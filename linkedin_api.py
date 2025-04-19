import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPID_API_KEY = os.getenv("RAPID_API_KEY")

def get_linkedin_jobs(keywords):
    url = "https://linkedin-data-api.p.rapidapi.com/search-jobs"
    headers = {
        "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com",
        "x-rapidapi-key": RAPID_API_KEY
    }
    params = {
        "keywords": keywords,
        "locationId": "103644278",
        "datePosted": "anyTime",
        "sort": "mostRelevant"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get("data", [])
    return []
    
def get_job_details(job_id):
    """Fetch full job details including description, responsibilities, etc."""
    url = "https://linkedin-data-api.p.rapidapi.com/get-job-details"
    headers = {
        "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com",
        "x-rapidapi-key": RAPID_API_KEY
    }
    params = {"id": job_id}
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json().get("data", {})
