from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from pathlib import Path
import re

from matcher import extract_text_from_pdf, extract_text_from_docx, match_resume_to_job

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5 MB
ALLOWED_EXTENSIONS = {"pdf", "docx", "txt"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def read_resume(uploaded_file):
    filename = secure_filename(uploaded_file.filename or "")
    extension = Path(filename).suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(uploaded_file)
    if extension == ".docx":
        return extract_text_from_docx(uploaded_file)
    if extension == ".txt":
        return uploaded_file.read().decode("utf-8", errors="ignore")
    return ""


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        job_description = request.form.get("job_description", "").strip()
        pasted_resume = request.form.get("resume_text", "").strip()
        resume_file = request.files.get("resume_file")
        resume_text = pasted_resume

        if resume_file and resume_file.filename:
            if not allowed_file(resume_file.filename):
                error = "Please upload a PDF, DOCX, or TXT resume."
            else:
                try:
                    resume_text = read_resume(resume_file).strip()
                except Exception:
                    error = "We couldn't read that file. Try a text-based PDF, DOCX, or TXT file."
        if not error and not resume_text:
            error = "Paste your resume text or upload a resume file."
        elif not error and len(job_description) < 30:
            error = "Please enter a job description with at least 30 characters."
        elif not error:
            result = match_resume_to_job(resume_text, job_description)

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
