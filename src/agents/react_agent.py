from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from src.config.settings import OPENAI_API_KEY
from src.tools.math_tools import multiply, divide


model = ChatOpenAI(
    model="gpt-5.6",
    api_key=xxxxxxxxxxxxxx
)

tools = [
    multiply,
    divide
]

agent = create_agent(
    model=model,
    tools=tools
)