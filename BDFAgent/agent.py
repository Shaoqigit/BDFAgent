from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate


class LLMConstructor:
    def __init__(self, api_key, base_url, model, other_params):
        """
        initiate the LLM constructor with the given parameters"""
        self.api_key = api_key
        self.base_url = base_url
        self.model = model
        self.params = other_params  # temperature and max_tokens

    
    def init_LLM(self):
        """
        construct llm model
        """
        self.model = ChatOpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
            model=self.model,
            temperature=self.params.get("temperature", 0.),
            max_tokens=self.params.get("max_tokens", 1024),
        )
        return self.model
    
    def init_prompt(self, prompts):
        """
        configure system prompts
        """
        self.prompt = ChatPromptTemplate.from_messages(prompts)

    def create_agent(self, tools, if_verbose=True, intermediate_steps=False, errors_handling=True):
        """
        create agent with the given tools and prompt""
        """
        self.agent = create_tool_calling_agent(self.model, tools, self.prompt)
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=tools,
            verbose=if_verbose,
            return_intermediate_steps=intermediate_steps,  # 启用中间步骤记录
            handle_parsing_errors=errors_handling)
        
        return self.agent_executor
    
    def generate_answer(self, question):
        """
        generate answer for the given question
        """
        response_chain = self.agent_executor
        result = response_chain.invoke({"input": question})
        return result

