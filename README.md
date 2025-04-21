# ResumeMatch 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://www.python.org/downloads/)  
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-red.svg)](https://flask.palletsprojects.com/)  
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT_Integration-lightgrey.svg)](https://openai.com/)
[![React](https://img.shields.io/badge/React-19.1.0-blue.svg)](https://reactjs.org/)

**Elevator Pitch**  
Job seekers spend hours tweaking their resumes and hunting for openings. ResumeMatch uses AI to instantly analyze and optimize your resume, match you to top roles, and even draft custom cover letters—saving you time and boosting your chances of landing interviews.

---

## 📋 Table of Contents

1. [Demo](#demo)  
2. [Features](#features)  
3. [Prerequisites](#prerequisites)  
4. [Installation](#installation)  
5. [Environment Variables](#environment-variables)  
6. [Usage](#usage)  
7. [Project Structure](#project-structure)  
8. [Built With](#built-with)  
9. [Roadmap](#roadmap)  
10. [Troubleshooting](#troubleshooting)  
11. [Contributing](#contributing)  
12. [License](#license)  
13. [Contact](#contact)  

---

### Inspiration
![Our Inspiration](assets/Inspiration.png)  
_We saw how Qualcomm's portal instantly matches resumes to their roles and thought: let's bring that power to UMBC students and beyond._

_Screenshots:_

| Landing Page |
|:------------:|
| ![Initial Page](assets/Initial_Page.png) |

| Matched Jobs  | Cover Letter |
|:-------------:|:------------:|
| ![Matched Jobs](assets/Matched_Jobs.png) | ![Cover Letter](assets/Cover_Letter.png) |

---

## ✨ Features
  
- **Job Matching**: Real LinkedIn job data via RapidAPI
- **Match Scoring**: Percentage match between your resume and job descriptions
- **Cover Letter Generation**: Tailored cover letters based on your resume and job description
---

## 🔧 Prerequisites

- Python **3.8+**  
- Node.js **16+** (for React frontend)
- A free RapidAPI account with **LinkedIn Jobs API**  
- An **OpenAI** account & API key  

---

## 🛠️ Installation

### Backend
```bash
# Clone
git clone https://github.com/sairambokka/resume-job-matcher.git
cd resume-job-matcher

# Setup venv
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows

# Install
pip install -r requirements.txt
```

### Frontend
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Build for production
npm run build
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```ini
OPENAI_API_KEY=your_openai_api_key
RAPID_API_KEY=your_rapidapi_key
```

## 🚀 Usage

### Development Mode
1. Start the backend server:
   ```bash
   python app.py
   ```

2. In a separate terminal, start the React frontend:
   ```bash
   cd frontend
   npm start
   ```

3. Visit `http://localhost:3000`

### Production Mode
1. Build the frontend:
   ```bash
   cd frontend
   npm run build
   ```

2. Start the server:
   ```bash
   python app.py
   ```

3. Visit `http://localhost:5000`

4. Upload your PDF resume

5. Explore:
   - Extracted skills
   - Matched jobs & cover letters
   - Match scores

## 📂 Project Structure

```
.
├── app.py                # Flask API routes & SQLite database integration
├── resume_utils.py       # PDF parsing & keyword extraction
├── linkedin_api.py       # LinkedIn RapidAPI integration
├── gpt_utils.py          # OpenAI GPT interactions
├── templates/            # HTML views
├── static/               # CSS & JS for server-rendered pages
├── frontend/             # React frontend application
│   ├── src/              # React components and logic
│   ├── public/           # Static assets
│   └── package.json      # Frontend dependencies
├── assets/               # Screenshots & demo materials
├── requirements.txt      # Python dependencies
├── README.md
└── .env                  # Environment variables (not included in repository)
```

## 🔨 Built With

- **Backend**:
  - [Flask](https://flask.palletsprojects.com/) - Web framework
  - [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) - Database ORM
  - [OpenAI GPT](https://openai.com/) - Natural language processing
  - [PyMuPDF](https://pymupdf.readthedocs.io/) - PDF parsing
  - [scikit-learn](https://scikit-learn.org/) - Keyword extraction

- **Frontend**:
  - [React](https://reactjs.org/) - UI framework
  - [React Router](https://reactrouter.com/) - Navigation
  - [Tailwind CSS](https://tailwindcss.com/) - Styling

- **Data**:
  - [RapidAPI](https://rapidapi.com/) - LinkedIn job data
  - [SQLite](https://www.sqlite.org/) - Local database

## 🛣️ Roadmap

- [x] Resume parsing & keyword extraction
- [x] Job search via LinkedIn API
- [x] Cover letter generation
- [x] Match scoring between resume and jobs
- [x] Modern React frontend
- [ ] User authentication & profile saving
- [ ] Export improved resume (PDF)
- [ ] Automated tests & CI pipeline
- [ ] Docker containerization
- [ ] Cloud deployment

## 🔮 Future Work

This application can be improved in several ways:

1. **LinkedIn API Integration**: Replace the third-party API with the official LinkedIn API when available.

2. **Enhanced Job Matching Algorithm**: Implement more sophisticated matching algorithms beyond GPT-based scoring.

3. **User Authentication**: Add account creation and resume storage functionality.

4. **Implement Skill Gap Analysis**: In-depth skill gap analysis with specific learning resources.

5. **Mobile App**: Develop companion mobile applications for iOS and Android.

## ❓ Troubleshooting

**Issue**: PDF parsing fails
**Solution**: Ensure your PDF is not password-protected and is in a readable format

**Issue**: No jobs appear after upload
**Solution**: Check your RapidAPI key and connection; try more general keywords

**Issue**: API rate limits
**Solution**: Implement caching or reduce the number of requests

**Issue**: Frontend not connecting to backend
**Solution**: Ensure the proxy setting in package.json is correct and both servers are running

## 🤝 Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature/name`
3. Commit: `git commit -m "Add feature"`
4. Push: `git push origin feature/name`
5. Open a PR — we'll review within 48 hours!

## 📜 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

## 📬 Contact

Sairam Bokka – sbokka1@umbc.edu  
Project Link: [https://github.com/sairambokka/resume-job-matcher](https://github.com/sairambokka/resume-job-matcher)