from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate

from BDFAgent.bdf_parser_Lc import tools

# 1. 初始化模型
llm = ChatOpenAI(
    api_key="sk-zcpmjwctlnkthagcorztornyziblyxvkjireovscqsymjqyn",
    # api_key="sk-597340b4a1944333ab72030ffa11c645",
    base_url="https://api.siliconflow.cn/v1",
    # base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="deepseek-ai/DeepSeek-V3",
    # model="qwen2.5-72b-instruct",
    # model="Qwen/QwQ-32B",
    temperature=0.,
    max_tokens=1024,
)

# 2. 定义工具（使用之前实现的BDF工具）

# 3. 创建包含必需变量的提示模板
prompt = ChatPromptTemplate.from_messages([
    ("system", """
    你是一个有限元分析助手，可以使用以下工具：
    NodeInfoQuery, ElementTypeQuery, MaterialPropertyQuery
    
    请按照以下规则响应：
    - 使用Markdown表格展示多组数据
    """),
    ("placeholder", "{agent_scratchpad}"),  # 关键占位符
    ("user", "{input}")
])

# 4. 创建Agent
agent = create_tool_calling_agent(llm, tools, prompt)

# 5. 创建执行器（需配置中间步骤处理）
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    # return_intermediate_steps=True,  # 启用中间步骤记录
    handle_parsing_errors=True)

# 6. 测试查询
# response = agent_executor.invoke({"input": "统计模型中的CQUAD4单元数量，并列出材料1的属性"})
# print(response["output"])
