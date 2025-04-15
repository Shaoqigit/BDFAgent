import yaml

from CAEAgent.agent import LLMConstructor
from CAEAgent.bdf_parser import BDFAnalyzer 
from CAEAgent.mesh_operators import MeshOperator
from CAEAgent.hyperworks_operator import HyperWorksOperator
from CAEAgent.tools import generate_BDF_tools, generate_mesh_tools, generate_hyperworks_tools

llm = LLMConstructor(api_key="sk-zcpmjwctlnkthagcorztornyziblyxvkjireovscqsymjqyn",
                     base_url="https://api.siliconflow.cn/v1",
                     model="Qwen/Qwen2.5-32B-Instruct",
                     other_params={"temperature": 0.5, "max_tokens": 1024})
llm.init_LLM()
# llm.init_prompt([
#     ("system", """
#     你是一个有限元分析助手，可以使用以下工具：
#     NodeInfoQuery, ElementTypeQuery, MaterialPropertyQuery
    
#     请按照以下规则响应：
#     - 使用Json格式展示多组数据
#     """),
#     ("placeholder", "{agent_scratchpad}"),  # 关键占位符
#     ("user", "{input}")
# ])

llm.init_prompt([
    ("system", """
    你是一个有限元分析高手，可以使用以下工具：
    NodeInfoQuery, ElementTypeQuery, MaterialPropertyQuery, MeshConverter, ImportBDF, GenerateMesh, RunSimulation
    """),
    ("placeholder", "{agent_scratchpad}"),  # 关键占位符
    ("user", "{input}")
])

bdf_file = "test_cases/CRM_V12wingbox_COARSE_1.bdf"
mesh_operator = MeshOperator(bdf_file)
mesh_tools = generate_mesh_tools(mesh_operator)

bdf_analyzer = BDFAnalyzer(bdf_file)
bdf_tools = generate_BDF_tools(bdf_analyzer)

# Add HyperWorks tools
hyperworks_model_path = "test_cases/cbush_test.bdf"
hyperworks_operator = HyperWorksOperator(hyperworks_model_path)
hyperworks_tools = generate_hyperworks_tools(hyperworks_model_path)

# Combine all tools
tools = bdf_tools + mesh_tools + hyperworks_tools

llm.create_agent(tools, if_verbose=True, intermediate_steps=False, errors_handling=True)

# 修改问题以使用正确的工具名称和路径
response = llm.generate_answer("导入BDF模型文件")
print("Question:", response["input"])
