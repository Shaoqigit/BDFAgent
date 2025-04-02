from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from BDFAgent.agent import LLMConstructor
from BDFAgent.bdf_parser import tools


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
llm.init_prompt([
    ("system", """
    你是一个有限元分析助手，可以使用以下工具：
    NodeInfoQuery, ElementTypeQuery, MaterialPropertyQuery
    
    请按照以下规则响应：
    - 使用Markdown表格展示多组数据
    """),
    ("placeholder", "{agent_scratchpad}"),  # 关键占位符
    ("user", "{input}")
])
llm.create_agent(tools, if_verbose=True, intermediate_steps=False, errors_handling=True)
response = llm.generate_answer("查询模型中的单元编号为129和120的单元属性，并列出材料1的属性")

print("Question:", response["input"])
