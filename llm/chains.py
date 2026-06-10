from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain_core.messages import HumanMessage

from config import OPENAI_API_KEY
from llm.prompts import SYSTEM_PROMPT

llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model="gpt-4o-mini",
    temperature=0.7
)

def ask_llm(question: str, context: str):

    response = llm.invoke([
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(
            content=f"""
            Context:
            {context}

            User Question:
            {question}
            """
        )
    ])

    return response.content