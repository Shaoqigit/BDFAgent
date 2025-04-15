import os
import subprocess

class MeshOperator:
    def __init__(self, mesh_path):
        self.mesh_path = mesh_path

    def _is_executable_available(self, executable_name):
        """Check if the given executable is available in the system PATH."""
        return any(
            os.path.isfile(os.path.join(path, executable_name)) and os.access(os.path.join(path, executable_name), os.X_OK)
            for path in os.environ["PATH"].split(os.pathsep)
        )

    def convert_mesh(self, outputmesh_path):
        print("---正在转换网格格式---")
        result = subprocess.run(
            ["meshio", "convert", "-i", "nastran", "-o", "gmsh22", f"{self.mesh_path}", f"{outputmesh_path}"], capture_output=True, text=True, check=True)
        return result.stdout
    
    def open_mesh(self, mesh_path):
        print("---正在打开网格文件---")
        
        # 检查Gmsh是否可用
        if not self._is_executable_available("gmsh"):
            raise FileNotFoundError("Gmsh executable not found. Please ensure Gmsh is installed and added to your system PATH.")
        
        result = subprocess.run(
            ["gmsh", mesh_path], capture_output=True, text=True, check=True)
        return result.stdout

    def convert_bdf_to_hw(self, output_hw_path):
        """
        使用pyNastran读取BDF文件并转换为Hypermesh格式 (.hw)
        """
        from pyNastran.bdf.bdf import BDF  # 导入pyNastran的BDF模块

        print("---正在将BDF文件转换为HW格式---")
        bdf_model = BDF(debug=False)
        bdf_model.read_bdf(self.mesh_path)  # 读取BDF文件

        # 假设需要添加网格划分逻辑，此处可以扩展
        # Example: bdf_model.add_mesh(...)

        # 将处理后的模型导出为HW格式
        bdf_model.write_hypermesh(output_hw_path)
        print(f"---已成功生成HW文件: {output_hw_path}---")

