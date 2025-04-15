import subprocess
import shlex
from pathlib import Path
import platform
from typing import Tuple, Optional
import sys
import os

from langchain.tools import tool
from pydantic import BaseModel, Field

class NastranRunner:
    def __init__(self, input_path: str, nastran_path: str = "nastran.exe"):
        # self.input_path = self._handle_input_path(input_path)  # 处理输入路径
        self.input_path = input_path  # 处理输入路径
        self.nastran_path = nastran_path  # 默认路径已经添加至环境变量
        
    def _validate_nastran_path(self, path: str) -> Path:
        """验证Nastran可执行文件存在"""
        # 尝试在系统PATH中查找
        result = subprocess.run(["Get-Command", f"{path}"], capture_output=True, text=True)
        if result.returncode == 0:
            return Path(result.stdout.strip())
        raise FileNotFoundError(f"Nastran executable not found at {path}")

    def _handle_special_paths(self, command: str) -> str:
        """处理含空格路径，添加双引号"""
        parts = []
        for part in shlex.split(command, posix=(platform.system() != 'Windows')):
            if str(Path(part).exists()) and ' ' in part:  # 路径存在且包含空格
                parts.append(f'"{part}"')
            else:
                parts.append(part)
        return ' '.join(parts)

    def _handle_input_path(self, path: str) -> str:
        """处理输入路径，确保路径正确"""
        self.input_path = str(Path(path).resolve())  # 转换为绝对路径
        if not Path(self.input_path).exists():
            raise FileNotFoundError(f"输入文件不存在: {self.input_path}")
        return self.input_path

    def _execute(
        self, 
        command: str=None,
        timeout: Optional[float] = None
    ) -> Tuple[int, str, str]:
        """
        执行Nastran命令
        :return: (return_code, stdout_output, stderr_output)
        """
        # 处理特殊字符和路径
        # safe_command = self._handle_special_paths(command)
        optional_commands = command.split(" ")[:-1]  # 提取可选命令
        safe_command = self.nastran_path + " " + " ".join(optional_commands) + " " + self.input_path
        if platform.system() == "Windows":
            args = safe_command
            shell = True  # Windows需要shell环境
        else:
            args = shlex.split(safe_command)
            shell = False

        try:
            proc = subprocess.Popen(
                args,
                shell=shell,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            
            # 实时输出捕获
            stdout_lines = []
            stderr_lines = []
            while True:
                stdout = proc.stdout.readline()  # type: ignore
                if stdout:
                    stdout_lines.append(stdout)
                    print(f"[NASTRAN] {stdout.strip()}")  # 实时输出
                    
                stderr = proc.stderr.readline()  # type: ignore
                if stderr:
                    stderr_lines.append(stderr)
                    print(f"[NASTRAN ERROR] {stderr.strip()}", file=sys.stderr)

                if proc.poll() is not None:
                    break

                if timeout is not None and (time.time() - start_time) > timeout:
                    proc.kill()
                    raise subprocess.TimeoutExpired(command, timeout)

            return_code = proc.poll()
            
        except Exception as e:
            error_msg = f"执行失败: {str(e)}"
            return (-1, "\n".join(stdout_lines), error_msg)

        return (
            return_code,
            "\n".join(stdout_lines),
            "\n".join(stderr_lines)
        )

    def execute_nastran_tool(self, command: str=None, working_dir: str=None) -> dict:
        """
        执行Nastran仿真任务
        必填参数:
        - command: 由输入文件路径和可选参数组合而成的完整命令，例如：
        'input.bdf memory=16gb'
        - working_dir: （可选）指定工作目录
        """
        print("------------执行Nastran任务-----------------")
        if working_dir:
            os.chdir(working_dir)  # 切换工作目录
        try:
            return_code, stdout, stderr = self._execute(command)
            output = {
                "status": "SUCCESS" if return_code == 0 else "ERROR",
                "return_code": return_code,
                "log": stdout,
                "f06_output": find_result_file("f06"),  # 自动查找结果文件
                "op2_output": find_result_file("op2"),
                "error": stderr
            }
        except Exception as e:
            output = {"status": "CRASHED", "error": str(e)}
        
        return output

def find_result_file(ext: str) -> Optional[str]:
    """自动查找最新结果文件"""
    files = list(Path.cwd().glob(f"*.{ext}"))
    if files:
        return str(max(files, key=lambda x: x.stat().st_ctime))
    return None


class NastranCommandInput(BaseModel):
    user_request: str = Field(...,
        description="用户自然语言描述的需求，例如'加载工况3的模型，分配16GB内存'")
    os_type: Optional[str] = Field(None,
        enum=["windows", "linux", "auto"],
        description="操作系统类型，auto为自动检测")
    default_memory: Optional[str] = Field("4gb", 
        description="当用户未指定内存时的默认值")
    enforce_safe_path: Optional[bool] = Field(True,
        description="是否启用路径安全校验")

@tool("generate_nastran_command", args_schema=NastranCommandInput)
def generate_command_tool(nastran_command_input: NastranCommandInput) -> str:
    """
    根据自然语言描述生成Nastran命令行
    参数示例:
    {{
        "user_request": "运行模型需要8核CPU", 
        "os_type": "auto"
    }}
    """
    try:
        # 自动检测操作系统类型
        detected_os = platform.system().lower()
        if nastran_command_input.os_type == "auto":
            target_os = "windows" if "windows" in detected_os else "linux"
        else:
            target_os = nastran_command_input.os_type
        
        # 调用之前的参数解析链
        params_chain = create_param_chain()  # 使用前面定义的解析链
        command_params = params_chain.invoke({"user_input": user_request})
        
        # 构建基础命令
        base_command = {
            "windows": f'nastran "{command_params["input_file"]}" scr=yes',
            "linux": f'nastran {command_params["input_file"]} scr=yes'
        }[target_os]
        
        # 添加资源参数
        flags = {"windows": "mem", "linux": "memory"}
        if command_params.get('memory'):
            base_command += f' {flags[target_os]}={command_params["memory"]}'
        else:
            base_command += f' {flags[target_os]}={default_memory}'
            
        if command_params.get('batch_mode') and target_os == "linux":
            base_command += " batch=yes"
        
        # 文件路径安全检查
        if enforce_safe_path:
            validate_filepath(command_params["input_file"])
            
        return base_command
    
    except Exception as e:
        return f"命令生成失败：{str(e)}"

def validate_filepath(path: str):
    """安全路径校验"""
    forbidden_chars = {"windows": ['<', '>', '|', '&'],
                       "linux": [';', '&', '|']}
    
    current_os = platform.system().lower() 
    for char in forbidden_chars.get(current_os, []):
        if char in path:
            raise ValueError(f"路径包含非法字符：{char}")
        
    if not Path(path).exists():
        raise FileNotFoundError("输入的BDF文件不存在")


if __name__ == "__main__":
    # 示例用法
    nastran_runner = NastranRunner()
    breakpoint()