import requests
from langchain_core.tools import tool

@tool
def fetch_jobs(role: str) -> dict:
    """
    Generates a Google search link for the given job role across multiple platforms like LinkedIn, Indeed, etc.
    """
    # Sanitize the role to make it URL-friendly
    query = f"{role} site:linkedin.com/jobs OR site:indeed.com OR site:unstop.com OR site:glassdoor.com"
    google_search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    
    return {"Google Search Link": google_search_url}

# Correct call using .invoke()
print(fetch_jobs.invoke('Web Developer'))
