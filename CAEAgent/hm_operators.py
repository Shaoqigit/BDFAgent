from langchain.tools import BaseTool
from pywintypes import com_error
import win32com.client

class HyperMeshTool(BaseTool):
    name = "hypermesh_automation"
    description = "用于HyperMesh二次开发的工具"
    
    def _init_hmsession(self):
        try:
            self.hm = win32com.client.Dispatch("HyperMeshv14.0.Application")
            self.hm.Interactive = 1  # 保持GUI可见
            return True
        except com_error as e:
            print(f"COM错误: {e}")
            return False

    def __init__(self):
        super().__init__()
        if not self._init_hmsession():
            raise RuntimeError("无法连接HyperMesh实例")


class GeometryCleanerTool(HyperMeshTool):
    name = "hm_geometry_clean"
    description = "执行几何清理操作"
    
    def _run(self, tolerance: float = 0.1):
        """执行几何清理的Tcl命令序列"""
        tcl_script = f"""
        *createmark surfaces 1 all
        *removetolerances surfaces 1 {tolerance}
        *rebuildedges surfaces 1 {tolerance}
        *redrawall
        """
        self.hm.cmd(tcl_script)
        return "几何清理完成"

class AutoMesherTool(HyperMeshTool):
    name = "hm_automesh"
    description = "自动网格划分工具"
    
    def _run(self, elem_size: float, mesh_type: str = "quad"):
        tcl_script = f"""
        *createmark surfaces 1 all
        *surfacemeshautomesh surfaces 1 {elem_size} {mesh_type} 15 0 1 1 0
        *createmark elements 1 all
        *qualitymark elements 1 warpage 0.95
        """
        results = self.hm.cmd(tcl_script)
        return f"网格划分完成，质量报告:\n{results}"


class LoadCaseTool(HyperMeshTool):
    name = "hm_loadcase"
    description = "创建载荷工况"
    
    def _run(self, lc_name: str, load_type: str, **params):
        param_str = " ".join(f"{k} {v}" for k,v in params.items())
        tcl_script = f"""
        *createentity loadcols name={lc_name}
        *createentity loadsteps name={lc_name}_step
        *dictionaryset loadsteps {lc_name}_step analysis {load_type}
        {param_str}
        """
        self.hm.cmd(tcl_script)
        return f"载荷工况 {lc_name} 创建成功"
