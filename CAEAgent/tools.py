from langchain_core.tools import StructuredTool

from CAEAgent.bdf_parser import BDFAnalyzer
from CAEAgent.mesh_operators import MeshOperator
from CAEAgent.hyperworks_operator import HyperWorksOperator


def generate_BDF_tools(bdf_analyzer: BDFAnalyzer):
    """
    generate tools from the given tool class
    """
    tools = [
        StructuredTool.from_function(func=bdf_analyzer.get_node_info,
                                     name="NodeInfoQuery",
                                     description="""查询有限元模型节点数据，输入格式示例：
                                     {{"node_ids": [1001,1002], "count_only": false}}"""),
        StructuredTool.from_function(func=bdf_analyzer.get_element_info,
                                     name="ElementTypeQuery",
                                     description="""按单元类型或者单元编号筛选元素，输入示例：
                                     {{"element_type": "CQUAD4", "property_details": true}}或者
                                     {{"element_ids": [129,120], "property_details": false}}"""),
        StructuredTool.from_function(
            func=bdf_analyzer.get_material_info,
            name="MaterialPropertyQuery",
            description="通过材料ID获取详细属性，输入示例：{{'material_id': 1}}")

    ]
    return tools


def generate_mesh_tools(mesh_operator: MeshOperator):
    """
    生成网格处理工具
    """
    tools = [
        StructuredTool.from_function(
            func=mesh_operator.convert_mesh,
            name="MeshConverter",
            description="""转换网格格式，输入示例：
            {{"outputmesh_path": "converted_mesh.msh"}}"""),
        StructuredTool.from_function(
            func=mesh_operator.open_mesh,
            name="MeshViewer",
            description="""使用Gmsh打开网格文件进行浏览
            打开网格文件，输入示例：
            {{"mesh_path": "converted_mesh.msh"}}""")
    ]
    return tools


def generate_hyperworks_tools(model_path):
    """
    Generate tools for HyperWorks operations using HyperWorksOperator methods directly.
    """
    operator = HyperWorksOperator(model_path)
    tools = [
        StructuredTool.from_function(
            func=operator.open_hyperworks,
            name="OpenHyperWorks",
            description="Open HyperWorks application."
        ),
        StructuredTool.from_function(  # 添加import_bdf功能
            func=operator.import_bdf,
            name="ImportBDF",
            description="Import a BDF file into HyperWorks."
        )
    ]
    return tools


if __name__ == "__main__":
    mesh_operator = MeshOperator("cbush_test.bdf")
    mesh_operator.convert_mesh("converted_mesh.msh")