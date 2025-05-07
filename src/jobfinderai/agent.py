from dotenv import load_dotenv
from langchain.agents import initialize_agent
from langchain_core.tools import Tool, tool
from langchain_groq.chat_models import ChatGroq


from src.jobfinderai.fetch_job import fetch_jobs

import os
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# ========== STEP 3: LangChain Agent with Groq ==========
def run_agent(role):
    llm = ChatGroq(model_name="llama3-8b-8192", temperature=0)

    # Make sure fetch_jobs is defined with proper metadata
    tools = [
        Tool(
            name="fetch_jobs",
            func=fetch_jobs,  # this should be a callable function
            description="Fetches recent job listings for a given job title."
        )
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        handle_parsing_errors=True,  # important for avoiding OutputParserException
        verbose=True
    )

    response = agent.run(f"Fetch recent job listings for {role}")
    return response

