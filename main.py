import yaml
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from BDFAgent.agent import LLMConstructor
from BDFAgent.bdf_parser import generate_BDF_tools, generate_mesh_tools, BDFAnalyzer, MeshOperator


# response_chain = (RunnablePassthrough.assign(analysis_results=agent_executor)
#                   |
#                   RunnablePassthrough.assign(formatted_response=lambda x: f"""
#         **Analysis Report**
        
#         ### Problem Description
#         {x['input']}
        
#         ### 原始数据
#         ```json
#         {x['analysis_results']['output']}
#         ```
        
#         ### 工程解释
#         {x['analysis_results']['intermediate_steps']}
#         """)
#                   | StrOutputParser())

# # 复杂查询处理
# question = """
# 统计模型中CQUAD4单元数量，并列出ID为1的材料属性，
# 最后检查节点1001到1005的Z坐标是否大于50mm
# """
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
    你是一个有限元分网格处理高手，　可以使用一下工具：
    MeshConverter
    
    """),
    ("placeholder", "{agent_scratchpad}"),  # 关键占位符
    ("user", "{input}")
])

mesh_operator = MeshOperator("CRM_V12wingbox_COARSE_1.bdf")
# mesh_operator.convert_mesh("converted_mesh.msh")
mesh_tools = generate_mesh_tools(mesh_operator)

bdf_analyzer = BDFAnalyzer("CRM_V12wingbox_COARSE_1.bdf")
bdf_tools = generate_BDF_tools(bdf_analyzer)

tools = bdf_tools + mesh_tools

llm.create_agent(tools, if_verbose=True, intermediate_steps=False, errors_handling=True)
# response = llm.generate_answer("把网格转化为gmsh格式且命名为converted_mesh.msh打开Gmsh浏览")
response = llm.generate_answer("1.查询模型中的单元编号为5417的单元属性 2.把网格转化为gmsh格式且命名为converted_mesh.msh打开Gmsh浏览")

print("Question:", response["input"])
