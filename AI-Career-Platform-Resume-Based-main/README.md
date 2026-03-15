---

# AI Career Platform

### Intelligent Career Recommendation Platform Using Resume Analytics

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-green)
![Status](https://img.shields.io/badge/Project-Active-success)

---

# Project Overview

The **AI Career Platform** is an intelligent web application designed to help job seekers improve their resumes and discover suitable job opportunities.

The platform analyzes resumes using **resume analytics techniques**, extracts skills, calculates an **ATS score**, identifies **skill gaps**, and recommends jobs based on the user's profile.

The system simulates how **Applicant Tracking Systems (ATS)** evaluate resumes and provides insights to help users optimize their resumes for job applications.

---

# Key Features

### User Authentication

* User Registration
* Secure Login
* Dashboard access

---

### Resume Upload & Processing

Users can upload their resumes in **PDF format**.

The system extracts:

* Resume text
* Technical skills
* Resume sections

---

### Resume Analyzer

The platform evaluates the resume and provides:

* ATS Score
* Extracted Skills
* Detected Career Domain
* Missing Skills
* Resume Improvement Suggestions

Example insights:

```
ATS Score: 78%

Detected Domain: Data Science

Missing Skills:
TensorFlow
Scikit-Learn
Docker
```

---

### AI-Based Resume Suggestions

The system analyzes the resume and suggests improvements such as:

* Add project descriptions
* Include certifications
* Add measurable achievements
* Include internships or work experience
* Improve skill coverage

---

### Job Recommendation System

The platform matches user skills with job requirements and calculates a **match percentage**.

### Recommended Jobs

Shows only jobs with:

```
Match Percentage ≥ 50%
```

These jobs are highly relevant to the user's profile.

Example:

```
Machine Learning Engineer — 82%
Data Scientist — 76%
Data Analyst — 65%
```

---

### Explore Jobs

Displays **all available jobs** sorted by match percentage.

Example:

```
Machine Learning Engineer — 82%
Data Scientist — 76%
Backend Developer — 40%
Cloud Engineer — 35%
DevOps Engineer — 25%
```

Users can directly **apply via LinkedIn job links**.

---

# Technology Stack

### Backend

* Python
* Flask

### Resume Processing

* pdfplumber

### Frontend

* HTML
* CSS
* Jinja Templates

### Data Handling

* Python Sets
* Skill Matching Algorithms

---

# System Architecture

```
User
  │
  ▼
Flask Web Application
  │
  ├── Resume Upload
  │
  ├── Resume Analyzer
  │     ├─ Skill Extraction
  │     ├─ Domain Detection
  │     ├─ ATS Score Calculation
  │     └─ Resume Suggestions
  │
  └── Job Recommender
        ├─ Match Score Calculation
        ├─ Recommended Jobs
        └─ Explore Jobs
```

---

# Project Structure

```
AI-Career-Platform
│
├── app.py
├── resume_analyzer.py
├── job_recommender.py
├── database.py
├── requirements.txt
│
├── templates
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── upload.html
│   ├── analyzer.html
│   ├── jobs.html
│   └── explore_jobs.html
│
├── static
│   └── style.css
│
└── uploads
```

---

# Installation

### Clone Repository

```
```

```
cd AI-Career-Platform
```

---

### Install Dependencies

```
pip install -r requirements.txt
```

---

### Run the Application

```
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

# Example Workflow

1. User logs in to the platform
2. Uploads resume
3. System extracts resume text
4. Skills are detected
5. ATS score is calculated
6. Domain is identified
7. Missing skills and suggestions are generated
8. Job roles are matched with user skills
9. User explores recommended or all jobs

---


# Future Enhancements

Possible improvements:

* Resume keyword optimization
* Skill gap learning recommendations
* AI-based resume rewriting
* Real-time job APIs
* Resume ranking visualization

---

# Author

**Vignesh Manku**
Computer Science and Engineering Student

GitHub
[https://github.com/Manku-Vignesh](https://github.com/Manku-Vignesh)

---

# License

This project is developed for **educational and research purposes**.

---

