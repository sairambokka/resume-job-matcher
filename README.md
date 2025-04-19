# ResumeMatch

A smart application that analyzes your resume, extracts key skills, matches you with relevant job postings, provides personalized feedback, and generates tailored cover letters.

## Demo

### Inspiration
![Inspiration](assets/Inspiration.png)
Our inspiration came from Qualcomm's website, where they allow candidates to upload resumes and match them with suitable jobs in their company based on resume content.

### Initial Page
![Initial Page](assets/Initial_Page.png)
The landing page where users can upload their resume for analysis.

### Keywords and Feedback
![Keywords and Feedback](assets/Keywords_and_Feedback.png)
This section displays extracted keywords from your resume and provides AI-generated feedback for improvement.

### Matched Jobs
![Matched Jobs](assets/Matched_Jobs.png)
Based on your resume's content, we find and display relevant job opportunities from LinkedIn.

### Skill Gap Analysis
![Skill Gap Analysis](assets/Skill_Gap_Analysis.png)
An analysis of skills you have versus skills required by the job market, helping you identify areas for growth.

### Cover Letter
![Cover Letter](assets/Cover_Letter.png)
Generates tailored cover letters for specific job applications based on your resume and the job description.

## Features

- **Resume Analysis**: Extracts text and keywords from PDF resumes
- **Skill Identification**: Uses AI to identify and refine key skills in your resume
- **Job Matching**: Finds relevant LinkedIn job postings based on your skills
- **Resume Feedback**: Provides AI-powered feedback on your resume
- **Skill Gap Analysis**: Identifies missing skills compared to job requirements
- **Cover Letter Generation**: Creates tailored cover letters for specific job applications

## Tech Stack

- **Backend**: Flask (Python)
- **NLP/AI**: OpenAI GPT for text analysis and generation
- **Document Processing**: PyMuPDF for PDF extraction
- **APIs**: LinkedIn job search integration
- **Frontend**: HTML, CSS, JavaScript

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/resume-job-matcher.git
   cd resume-job-matcher
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   LINKEDIN_API_KEY=your_linkedin_api_key
   ```

## Usage

1. Start the application:
   ```
   python app.py
   ```

2. Open your browser and navigate to `http://localhost:5000`

3. Upload your resume (PDF format)

4. View your extracted skills, matching jobs, and personalized feedback

5. Generate cover letters for specific job applications

## Project Structure

- `app.py`: Main Flask application
- `resume_utils.py`: Resume parsing and keyword extraction
- `linkedin_api.py`: LinkedIn job search integration
- `gpt_utils.py`: OpenAI GPT integration for text analysis and generation
- `templates/`: HTML templates for the web interface
- `static/`: CSS, JavaScript, and static assets

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- [OpenAI](https://openai.com/) for GPT API
- [LinkedIn](https://www.linkedin.com/) for job data
- All contributors and testers