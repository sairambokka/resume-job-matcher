from flask import Flask, render_template, request
from resume_utils import extract_keywords, extract_text_from_pdf
from linked_api import get_linkedin_jobs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    job_results = []
    keywords = []
    if request.method == "POST":
        file = request.files["resume"]
        if file:
            text = extract_text_from_pdf(file.stream)
            keywords = extract_keywords(text)
            # Only proceed if we have keywords
            if len(keywords) > 0:
                query = " ".join(keywords[:5])
                job_results = get_linkedin_jobs(query)
            else:
                keywords = []  # Ensure it's a regular list

    return render_template("index.html", keywords=keywords, job_results=job_results)

if __name__ == "__main__":
    app.run(debug=True)

