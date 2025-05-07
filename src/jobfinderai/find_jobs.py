from src.jobfinderai.agent import run_agent
from src.jobfinderai.fetch_job import fetch_jobs

def jobs_recommended(predicted_role:str):

    job_results = run_agent(predicted_role)
    print("\n📄 Recommended Jobs:\n", job_results)
    return job_results