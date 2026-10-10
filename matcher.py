import re
from io import BytesIO

import fitz  # PyMuPDF
from docx import Document

# Beginner-friendly skill list. You can expand this for your target roles.
SKILLS = [
    "python", "java", "c", "c++", "sql", "html", "css", "javascript",
    "flask", "django", "react", "node.js", "git", "github", "excel",
    "power bi", "tableau", "machine learning", "deep learning", "nlp",
    "data analysis", "data structures", "algorithms", "oops",
    "object oriented programming", "dbms", "operating systems",
    "computer networks", "communication", "problem solving", "testing",
    "rest api", "mongodb", "mysql", "postgresql", "aws", "azure",
    "linux", "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
    "fastapi", "bootstrap", "typescript", "api", "statistics"
]


def extract_text_from_pdf(file_storage):
    data = file_storage.read()
    pages = []
    with fitz.open(stream=data, filetype="pdf") as pdf:
        for page in pdf:
            pages.append(page.get_text())
    return "\n".join(pages)


def extract_text_from_docx(file_storage):
    document = Document(BytesIO(file_storage.read()))
    return "\n".join(paragraph.text for paragraph in document.paragraphs)


def find_skills(text):
    normalized = text.lower()
    found = []
    for skill in SKILLS:
        # Match whole words for short skills, and exact phrase boundaries generally.
        pattern = r"(?<![a-z0-9+#.])" + re.escape(skill) + r"(?![a-z0-9+#.])"
        if re.search(pattern, normalized):
            found.append(skill)
    return sorted(set(found))


def match_resume_to_job(resume_text, job_description):
    resume_skills = find_skills(resume_text)
    job_skills = find_skills(job_description)

    matched = sorted(set(resume_skills) & set(job_skills))
    missing = sorted(set(job_skills) - set(resume_skills))
    # Score is based on skills detected in the job description, not a hiring probability.
    score = round((len(matched) / len(job_skills)) * 100) if job_skills else 0

    return {
        "score": score,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched,
        "missing_skills": missing,
        "job_skill_count": len(job_skills),
        "note": (
            "This score measures overlap between the skills detected in the resume "
            "and job description. It is not an ATS score or a prediction of hiring."
        ),
    }
