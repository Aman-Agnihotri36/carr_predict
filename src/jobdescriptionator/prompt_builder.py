from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv
import os


load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

llm = ChatGroq(temperature=0.7, model_name="llama3-8b-8192")

def build_prompt(profile: dict, predicted_role: str) -> str:
    return f"""
A student has the following profile:
{profile} and you are a experienced professional in that profile. Your response should be like an ai directly speaking to the student

The predicted job role is: "{predicted_role}".

1. Explain why this job role was predicted.
2. What can the student do to improve their fit for this role?
"""

def get_explanation(profile: dict, predicted_role: str) -> str:
    messages = [
        SystemMessage(content="You are a helpful career counselor."),
        HumanMessage(content=build_prompt(profile, predicted_role))
    ]
    response = llm(messages)
    return response.content