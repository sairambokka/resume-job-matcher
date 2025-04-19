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

def generate_resume_feedback(resume_text, role_focus="internship"):
    system_msg = {
        "role": "system",
        "content": (
            "You are an expert career coach with 10+ years of experience helping "
            "students land internships and entry-level roles."
        )
    }
    user_msg = {
        "role": "user",
        "content": (
            f"Here is a student's resume text focused on {role_focus} roles. "
            "1) Give up to 5 specific improvement suggestions "
            "(action verbs, metrics, formatting, keywords). "
            "2) Provide one example of a rewritten bullet for their top experience.\n\n"
            f"{resume_text}"
        )
    }
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[system_msg, user_msg],
        temperature=0.7,
        max_tokens=400
    )
    return resp.choices[0].message.content

def generate_gap_feedback(resume_kw, all_job_kw):
    prompt = (
        f"The candidate's resume includes: {', '.join(resume_kw)}.\n"
        f"Top jobs require: {', '.join(all_job_kw)}.\n"
        "Identify the top 5 missing skills and suggest how they can be acquired or highlighted."
    )
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a career coach."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=200
    )
    return resp.choices[0].message.content

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