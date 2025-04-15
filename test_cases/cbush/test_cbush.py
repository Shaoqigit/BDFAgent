import yaml

from CAEAgent import nastran_runner
from CAEAgent.agent import LLMConstructor
from CAEAgent.bdf_parser import BDFAnalyzer 
from CAEAgent.mesh_operators import MeshOperator
from CAEAgent.nastran_runner import NastranRunner
from CAEAgent.tools import generate_BDF_tools, generate_mesh_tools, generate_nastran_tools


llm = LLMConstructor(api_key="sk-zcpmjwctlnkthagcorztornyziblyxvkjireovscqsymjqyn",
                     base_url="https://api.siliconflow.cn/v1",
                     model="Qwen/Qwen2.5-32B-Instruct",
                     other_params={"temperature": 0.5, "max_tokens": 1024})
llm.init_LLM()
llm.init_prompt([
    ("system", """
    你是一个有限元分析高手，　可以使用一下工具：
    NodeInfoQuery, ElementTypeQuery, MaterialPropertyQuery, MeshConverter, MeshViewer, execute_nastran
    
    """),
    ("placeholder", "{agent_scratchpad}"),  # 关键占位符
    ("user", "{input}")
])

bdf_file = "cbush_test.bdf"
mesh_operator = MeshOperator(bdf_file)
mesh_tools = generate_mesh_tools(mesh_operator)

bdf_analyzer = BDFAnalyzer(bdf_file)
bdf_tools = generate_BDF_tools(bdf_analyzer)

nastran_runner = NastranRunner(bdf_file)
nastran_tools = generate_nastran_tools(nastran_runner)  # 确保这个函数返回了一个列表，每个元素都是一个 StructuredTool 或其他可调用对象。如果没有，请检查函数实现或确保函数返回了正确的工具列表。

tools = bdf_tools + mesh_tools + nastran_tools

llm.create_agent(tools, if_verbose=True, intermediate_steps=False, errors_handling=True)
# response = llm.generate_answer("把网格转化为gmsh格式且命名为converted_mesh.msh打开Gmsh浏览")
response = llm.generate_answer("1.查询模型中的单元编号为128的单元属性 2.运行nastran去执行这个BDF仿真任务 3.把网格转化为gmsh格式且命名为converted_mesh.msh打开Gmsh浏览")

print("Question:", response["input"])
