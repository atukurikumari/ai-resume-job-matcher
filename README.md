# AI Resume-to-Job Matcher

A beginner-friendly web app that compares skills detected in resume text with skills mentioned in a job description.

## Features
- Paste resume text or upload a PDF, DOCX, or TXT resume
- Paste a job description
- See matching skills and missing skills
- Get a simple skill-overlap percentage
- Responsive layout

## Tech stack
- Python
- Flask
- HTML and CSS
- PyMuPDF (PDF text extraction)
- python-docx (DOCX text extraction)
- Basic rule-based text matching

## Run on Windows
1. Install Python 3.10 or newer.
2. Extract this project folder.
3. Open Command Prompt or the VS Code terminal in this folder.
4. Create a virtual environment:
   ```bash
   py -m venv .venv
   ```
5. Activate it:
   ```bash
   .venv\Scripts\activate
   ```
6. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
7. Start the app:
   ```bash
   python app.py
   ```
8. Open the local address printed in the terminal (usually http://127.0.0.1:5000).

## Important limitations
- The percentage is a basic overlap score for skills in this project's built-in list, not a real ATS score or hiring prediction.
- The skill list in `matcher.py` is intentionally simple and can be expanded.
- Scanned/image-only PDFs may not contain extractable text; use a text-based PDF or paste the resume text.
- This starter app does not save uploaded resumes to disk or send them to an external AI service.
- Do not use `debug=True` in a public production deployment.

## Future improvements
- Add more skills and synonyms
- Add unit tests
- Add a downloadable analysis report
- Add semantic matching with a documented NLP model
- Deploy securely with production settings
