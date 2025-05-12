# from langchain_groq import ChatGroq
# from langchain.schema import HumanMessage, SystemMessage
# import os
# from dotenv import load_dotenv
# import os


# load_dotenv()

# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# llm = ChatGroq(temperature=0.7, model_name="llama3-8b-8192")

# def build_prompt(profile: dict, predicted_role: str) -> str:
#     return f"""


# A student has the following profile:
# {profile}

# You are an experienced professional in that profile. Your response should be like an AI directly speaking to the student.

# The predicted job role is: "{predicted_role}".

# Please return your response strictly in the following JSON array format (no extra text):
# """


# def get_explanation(profile: dict, predicted_role: str) -> str:
#     messages = [
#         SystemMessage(content="You are a helpful career counselor."),
#         HumanMessage(content=build_prompt(profile, predicted_role))
#     ]
#     response = llm(messages)
#     return response.content


from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
import os
import json
from dotenv import load_dotenv

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

llm = ChatGroq(temperature=0.7, model_name="llama3-8b-8192")

def build_prompt(profile: dict, predicted_role: str) -> str:
    return f"""
A student has the following profile:
{profile}

You are an experienced career counselor specialized in the field of "{predicted_role}". The student is seeking advice based on their profile and predicted role.

Your task is to return a **JSON object** that helps guide the student clearly.

❗ Your output must be a single **valid JSON array** with exactly one object that contains the following keys:
- "Job/Higher Studies?": either "Job" or "Higher Studies" based on the profile.
- "Reasoning": a short explanation (2–3 lines) justifying the choice.
- "Recommendations": an array of 5–6 bullet-point career actions or learning steps tailored to the role.
- "Career Tips": an array of 5–6 tips specifically helpful for this field.

Respond ONLY with valid JSON — no extra text.

Example format:
[
  {{
    "Job/Higher Studies?": "Job",
    "Reasoning": "Because of your strong practical and technical background, entering the industry would be most beneficial.",
    "Recommendations": [
      "Take courses in advanced databases.",
      "Contribute to open-source DBMS projects.",
      ...
    ],
    "Career Tips": [
      "Strengthen your SQL skills.",
      "Follow top database engineers on LinkedIn.",
      ...
    ]
  }}
]
"""


def get_explanation(profile: dict, predicted_role: str) -> list:
    messages = [
        SystemMessage(content="You are a helpful career counselor."),
        HumanMessage(content=build_prompt(profile, predicted_role))
    ]
    response = llm(messages)

    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        # If the model response is not valid JSON, return an empty list or handle accordingly
        return []
