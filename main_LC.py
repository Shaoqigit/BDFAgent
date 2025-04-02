from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from BDFAgent.agent_Lc import agent_executor

response_chain = (RunnablePassthrough.assign(analysis_results=agent_executor)
                  |
                  RunnablePassthrough.assign(formatted_response=lambda x: f"""
        **Analysis Report**
        
        ### Problem Description
        {x['input']}
        
        ### 原始数据
        ```json
        {x['analysis_results']['output']}
        ```
        
        ### 工程解释
        {x['analysis_results']['intermediate_steps']}
        """)
                  | StrOutputParser())

# 复杂查询处理
question = """
统计模型中CQUAD4单元数量，并列出ID为1的材料属性，
最后检查节点1001到1005的Z坐标是否大于50mm
"""

# result = response_chain.invoke({"input": question})
# print(result)

# response = agent_executor.invoke(
#     {"input": "查询模型中的单元编号为129和120的单元属性，并列出材料1的属性"})
response = agent_executor.invoke(
    {"input": "1.查询模型中的单元编号为129和120的单元属性"
     "2.列出材料1的属性"})
print("Question:", response["input"])
# print('response:', response["output"])
