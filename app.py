from flask import Flask, render_template, request, session
from resume_utils import extract_text_from_pdf, extract_keywords
from linkedin_api import get_linkedin_jobs, get_job_details
from gpt_utils import (
    refine_keywords_for_job,
    generate_resume_feedback,
    generate_gap_feedback,
    generate_cover_letter
)

app = Flask(__name__)
app.secret_key = "change_this_to_a_random_string"

@app.route("/", methods=["GET", "POST"])
def index():
    keywords, refined, jobs, feedback, gap_feedback = [], [], [], None, None

    if request.method == "POST":
        file = request.files["resume"]
        if file:
            text = extract_text_from_pdf(file.stream)
            session["last_resume_text"] = text

            # 1. Extract & refine keywords
            keywords = extract_keywords(text)
            if keywords is not None and len(keywords) > 0:
                refined = refine_keywords_for_job(keywords)

                # 2. Fetch matching jobs
                if refined:
                    query = " ".join(refined)
                    jobs = get_linkedin_jobs(query)

                # 3. GPT-powered resume feedback
                feedback = generate_resume_feedback(text, role_focus="cybersecurity internship")

                # 4. Skill-gap analysis
                if jobs:
                    all_job_kw = {kw for job in jobs for kw in job.get("keywords", [])}
                    gap_feedback = generate_gap_feedback(keywords, all_job_kw)
            else:
                keywords = []  # Ensure it's a regular list

    return render_template(
        "index.html",
        keywords=keywords,
        refined=refined,
        jobs=jobs,
        feedback=feedback,
        gap_feedback=gap_feedback
    )

@app.route("/cover-letter")
def cover_letter():
    resume_text = session.get("last_resume_text", "")
    job_id = request.args.get("job_id")
    job = get_job_details(job_id)

    prompt = (
        f"Candidate background:\n{resume_text[:2000]}\n\n"
        f"Role: {job['title']} at {job['company']['name']}\n\n"
        "Here is the full job description and requirements:\n"
        f"{job.get('description','')}\n\n"
        "Write a concise 200–250 word cover letter introduction that:\n"
        "1) Highlights why this candidate is a strong fit.\n"
        "2) References specific points from the role description."
    )
    letter = generate_cover_letter(prompt)

    return render_template("cover_letter.html", letter=letter, job=job)

if __name__ == "__main__":
    app.run(debug=True)
