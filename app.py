from flask import Flask, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from utils.resume_utils import extract_text_from_pdf, extract_keywords
from utils.linkedin_api import get_linkedin_jobs, get_job_details
from utils.gpt_utils import (
    refine_keywords_for_job,
    generate_cover_letter,
    build_cover_letter_prompt,
    generate_match_score
)

app = Flask(__name__)
app.secret_key = "change_this_to_a_random_string"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Job(db.Model):
    __tablename__ = 'jobs'
    id       = db.Column(db.String, primary_key=True)
    title    = db.Column(db.String, nullable=False)
    company  = db.Column(db.String, nullable=False)
    location = db.Column(db.String)
    url      = db.Column(db.String)
    benefits = db.Column(db.String)

    def to_dict(self):
        return {
            'id':       self.id,
            'title':    self.title,
            'company':  {'name': self.company},
            'location': self.location,
            'url':      self.url,
            'benefits': self.benefits
        }

@app.route('/api/jobs', methods=['GET'])
def api_jobs():
    jobs = Job.query.all()
    return jsonify({ 'jobs': [ j.to_dict() for j in Job.query.all() ] })

@app.route('/api/cover-letter', methods=['POST'])
def api_cover_letter():
    """
    Expects JSON body: { "resume": "<text>", "jobId": "<id>" }
    """
    data = request.get_json(force=True)
    resume_text = data.get("resume", "") or session.get("last_resume_text", "")
    job_id = data.get("jobId")
    if not (resume_text and job_id):
        return jsonify({"error": "resume text and jobId required"}), 400

    job = get_job_details(job_id)
    prompt = build_cover_letter_prompt(resume_text, job)
    letter = generate_cover_letter(prompt)

    match = generate_match_score(resume_text, job.get("description", ""))

    return jsonify({'letter': letter, 'job': job, 'match': match})

@app.route('/api/refresh-jobs', methods=['POST'])
def api_refresh_jobs():
    # 1. Read & store resume text
    file = request.files.get('resume')
    if not file:
        return jsonify({'error': 'No resume uploaded'}), 400

    text = extract_text_from_pdf(file.stream)
    session['last_resume_text'] = text

    # 2. Extract & refine keywords
    keywords = extract_keywords(text)
    refined  = refine_keywords_for_job(keywords)
    query    = ' '.join(refined[:5])

    # 3. Fetch from LinkedIn
    raw_jobs = get_linkedin_jobs(query)

    # 4. Persist into SQLite
    Job.query.delete()
    for j in raw_jobs:
        job = Job(
            id       = j['id'],
            title    = j['title'],
            company  = j['company']['name'],
            location = j.get('location',''),
            url      = j['url'],
            benefits = j.get('benefits','')
        )
        db.session.add(job)
    db.session.commit()

    # 5. Return the newly stored jobs
    return jsonify({ 'jobs': [ j.to_dict() for j in Job.query.all() ] })

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
