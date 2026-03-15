from flask import Flask, render_template, request, redirect, session
import os
from werkzeug.utils import secure_filename
from resume_analyzer import extract_skills
from resume_analyzer import analyze_resume
from database import *
from job_recommender import get_all_jobs_with_match, get_recommended_jobs

app = Flask(__name__)
app.secret_key = "career-platform-secret"

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

init_db()


@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET","POST"])
def login():

    error = None

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = login_user(email,password)

        if user:
            session["user"] = user[1]
            session["user_id"] = user[0]
            return redirect("/dashboard")
        else:
            error = "Invalid email or password"

    return render_template("login.html", error=error)


# ---------------- SIGNUP ----------------

@app.route("/signup", methods=["GET","POST"])
def signup():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        create_user(username,email,password)

        return redirect("/login")

    return render_template("signup.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    resume = get_last_resume(session["user_id"])

    skills = []
    ats_score = 0
    jobs = []

    if resume:

        path = resume[2]

        if os.path.exists(path):

            result = analyze_resume(path)

            skills = result["skills"]
            ats_score = result["ats_score"]

            jobs = get_recommended_jobs(skills)

        else:
            resume = None

    return render_template(
        "dashboard.html",
        username=session["user"],
        resume=resume,
        skills=[s.title() for s in skills],
        ats_score=ats_score,
        jobs=jobs[:3]
    )

# ---------------- UPLOAD ----------------

@app.route("/upload", methods=["GET","POST"])
def upload():

    message = None

    if request.method == "POST":

        if "resume" not in request.files:
            message = "Please select a resume file."
            return render_template("upload.html", message=message)

        file = request.files["resume"]

        if file.filename == "":
            message = "Please choose a file."
            return render_template("upload.html", message=message)

        # Validate file type
        if not file.filename.lower().endswith(".pdf"):
            message = "Only PDF files are allowed."
            return render_template("upload.html", message=message)

        filename = secure_filename(file.filename)

        path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        file.save(path)

        skills = extract_skills(path)

        save_resume(session["user_id"], path, ",".join(skills))

        return redirect("/analyze")

    return render_template("upload.html", message=message)


# ---------------- ANALYZER ----------------

@app.route("/analyze")
def analyze():

    if "user" not in session:
        return redirect("/login")

    resume = get_last_resume(session["user_id"])

    if not resume:
        return redirect("/upload")

    path = resume[2]

    # Check if file exists
    if not os.path.exists(path):
        return render_template(
            "upload.html",
            message="Resume file not found. Please upload your resume again."
        )

    result = analyze_resume(path)

    return render_template(
        "analyzer.html",
        skills=[s.title() for s in result["skills"]],
        domain=result["domain"],
        missing=[s.title() for s in result["missing_skills"]],
        suggestions=result["suggestions"],
        score=result["ats_score"]
    )
# ---------------- JOBS ----------------

@app.route("/jobs")
def jobs():
    resume = get_last_resume(session["user_id"])
    if not resume:
        return redirect("/upload")
    skills = resume[3].split(",")
    jobs = get_recommended_jobs(skills)
    return render_template("jobs.html", jobs=jobs)
#------------------------ALL JOBS---------------------------
@app.route("/explore_jobs")
def explore_jobs():

    resume = get_last_resume(session["user_id"])

    skills = []

    if resume:
        skills = resume[3].split(",")
        jobs = get_all_jobs_with_match(skills)

    return render_template(
        "explore_jobs.html",
        jobs=jobs
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)