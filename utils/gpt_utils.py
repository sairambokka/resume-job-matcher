import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def refine_keywords_for_job(keywords):
    system_msg = {
        "role": "system",
        "content": "You are a concise recruiter assistant who filters out generic or irrelevant resume keywords."
    }
    user_msg = {
        "role": "user",
        "content": (
            f"I extracted these keywords from a resume:\n{keywords}\n\n"
            "Return only those keywords that are most likely to help in matching tech jobs—"
            "remove any generic or irrelevant terms."
        )
    }
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[system_msg, user_msg],
        temperature=0.0,
        max_tokens=100
    )
    return [k.strip() for k in resp.choices[0].message.content.split(",")]

def generate_cover_letter(prompt):
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional cover letter writer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=400
    )
    return resp.choices[0].message.content

def build_cover_letter_prompt(resume_text, job):
    return (
        f"Candidate background:\n{resume_text[:2000]}\n\n"
        f"Role: {job['title']} at {job['company']['name']}\n\n"
        "Here is the full job description and requirements:\n"
        f"{job.get('description','')}\n\n"
        "Write a concise (200–250 word) cover letter introduction that:\n"
        "1) Highlights why this candidate is a strong fit.\n"
        "2) References specific points from the role description."
    )

def generate_match_score(resume_text: str, job_description: str) -> int:
    """
    Ask GPT to score how well the resume matches the job description, 0–100.
    Returns an integer percentage.
    """
    system_msg = {
        "role": "system",
        "content": "You are an expert recruiter. Given a candidate resume and a job description, "
                   "you rate how well the candidate matches the role on a scale from 0 to 100. "
                   "Return only the integer number."
    }
    user_msg = {
        "role": "user",
        "content": (
            f"Resume:\n{resume_text[:2000]}\n\n"
            f"Job Description:\n{job_description[:2000]}\n\n"
            "Respond with a single integer (0–100)."
        )
    }
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[system_msg, user_msg],
        temperature=0.0,
        max_tokens=5
    )
    # strip out anything non‑digit
    pct = ''.join(filter(str.isdigit, resp.choices[0].message.content))
    return int(pct) if pct else 0