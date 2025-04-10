
from pyNastran.bdf.bdf import BDF
from typing import Optional, List


class BDFAnalyzer:
    def __init__(self, filepath):
        self.model = BDF()
        self.model.read_bdf(filepath)

    def get_node_info(self,
                      node_ids: Optional[List[int]] = None,
                      count_only: bool = False):
        """获取节点信息，支持批量查询或计数"""
        print("---正在获取节点信息---")
        if count_only:
            return {"node_count": len(self.model.nodes)}

        return {
            nid: {
                "x": self.model.nodes[nid].x,
                "y": self.model.nodes[nid].y,
                "z": self.model.nodes[nid].z,
                "cp": self.model.nodes[nid].cp
            }
            for nid in node_ids
        }

    def get_element_info(self,
                         element_type: str = None,
                         element_ids: Optional[List[int]] = None,
                         property_details: bool = False):
        """获取指定类型单元信息"""
        print("---正在获取单元信息---")
        if element_ids is None:
            elements = [
                elem for elem in self.model.elements.values()
                if elem.type == element_type.upper()
            ]
        else:
            elements = [self.model.elements[eid] for eid in element_ids]

        if not property_details:
            return {"count": len(elements)}

        elem_dicts = []
        for elem in elements:
            if elem.type != "CQUAD4":
                elem_dicts.append({
                    "type": elem.type,
                    "eid": elem.eid,
                    "nodes": elem.node_ids,
                    "pid": elem.pid
                })
            else:
                elem_dicts.append({
                    "type":
                    elem.type,
                    "eid":
                    elem.eid,
                    "nodes":
                    elem.node_ids,
                    "pid":
                    elem.pid,
                    "material_id":
                    self.model.properties[elem.pid].Mid
                })
        return elem_dicts

    def get_material_info(self, material_id: int):
        """获取材料详细信息"""
        try:
            mat = self.model.materials[material_id]
            print(
                "material_info", {
                    "E": mat.E(),
                    "nu": mat.nu,
                    "rho": mat.rho,
                    "type": type(mat).__name__
                })
            return {
                "E": mat.E(),
                "nu": mat.nu,
                "rho": mat.rho,
                "type": type(mat).__name__
            }
        except KeyError:
            return {"error": f"Material {material_id} not found"}
        


