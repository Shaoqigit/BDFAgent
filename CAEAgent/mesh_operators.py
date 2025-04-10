import subprocess

class MeshOperator:
    def __init__(self, mesh_path):
        self.mesh_path = mesh_path

    def convert_mesh(self, outputmesh_path):
        print("---正在转换网格格式---")
        result = subprocess.run(
            ["meshio", "convert", "-i", "nastran", "-o", "gmsh22", f"{self.mesh_path}", f"{outputmesh_path}"], capture_output=True, text=True, check=True)
        return result.stdout
    
    def open_mesh(self, mesh_path):
        print("---正在打开网格文件---")
        result = subprocess.run(
            ["gmsh", f"{mesh_path}"], capture_output=True, text=True, check=True)
        return result.stdout