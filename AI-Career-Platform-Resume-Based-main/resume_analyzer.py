import pdfplumber

# Known skill database
SKILL_DATABASE = {
    "Data Science": ["python", "pandas", "numpy", "machine learning", "sql", "matplotlib"],
    "Web Development": ["html", "css", "javascript", "react", "node", "mongodb"],
    "Cloud": ["aws", "docker", "kubernetes", "terraform", "linux"],
    "Devops": ["docker", "kubernetes", "ci/cd", "jenkins", "git"],
    "Cyber": ["networking", "linux", "penetration testing", "security"]
}

COMMON_SKILLS = [
    "python","sql","java","docker","aws","machine learning","pandas",
    "html","css","javascript","react","node","linux","git","kubernetes"
]

def calculate_ats(skills, text):

    score = 0

    # Skill score
    score += min(len(skills) * 8, 40)

    # Sections score
    if "experience" in text:
        score += 10

    if "projects" in text:
        score += 10

    if "education" in text:
        score += 5

    if "skills" in text:
        score += 10

    if "certification" in text:
        score += 10

    return min(score,100)

def extract_text(resume_path):

    text = ""

    with pdfplumber.open(resume_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    return text.lower()


def extract_skills(resume_path):

    text = extract_text(resume_path)

    found_skills = []

    for skill in COMMON_SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def detect_domain(skills):

    domain_score = {}

    for domain, domain_skills in SKILL_DATABASE.items():

        score = len(set(skills).intersection(domain_skills))

        domain_score[domain] = score

    detected_domain = max(domain_score, key=domain_score.get)

    return detected_domain


def suggest_skills(domain, skills):

    domain_skills = SKILL_DATABASE.get(domain, [])

    missing_skills = list(set(domain_skills) - set(skills))

    return missing_skills[:5]


def generate_suggestions(skills, resume_text, domain):

    suggestions = []

    word_count = len(resume_text.split())

    # Check resume length
    if word_count < 200:
        suggestions.append("Your resume is too short. Add more project descriptions and technical experience.")

    # Check important sections
    if "projects" not in resume_text:
        suggestions.append("Add a Projects section with real-world implementations relevant to your domain.")

    if "experience" not in resume_text and "internship" not in resume_text:
        suggestions.append("Include internship or work experience to strengthen your profile.")

    if "education" not in resume_text:
        suggestions.append("Add an Education section clearly mentioning degree and institution.")

    if "skills" not in resume_text:
        suggestions.append("Add a dedicated Skills section listing your technical skills.")

    # Skill quantity check
    if len(skills) < 5:
        suggestions.append("Add more technical skills related to your domain to improve ATS ranking.")

    # Domain-based suggestions
    if domain == "Data Science":
        suggestions.append("Consider adding experience with TensorFlow, Scikit-learn, or data visualization tools.")

    if domain == "Web Development":
        suggestions.append("Include frontend frameworks like React or backend technologies like Node.js.")

    if domain == "Cloud":
        suggestions.append("Mention cloud platforms like AWS, Azure, or GCP along with deployment projects.")

    # Check achievements
    if "%" not in resume_text and "improved" not in resume_text:
        suggestions.append("Include measurable achievements such as 'Improved model accuracy by 15%'.")

    # Check certifications
    if "certification" not in resume_text:
        suggestions.append("Include certifications relevant to your domain to strengthen credibility.")

    return suggestions[:6]


def analyze_resume(resume_path):

    text = extract_text(resume_path)

    skills = []

    for skill in COMMON_SKILLS:
        if skill in text:
            skills.append(skill)

    domain = detect_domain(skills)

    missing_skills = suggest_skills(domain, skills)

    suggestions = generate_suggestions(skills, text, domain)

    ats_score = calculate_ats(skills, text)

    return {
        "skills": skills,
        "domain": domain,
        "missing_skills": missing_skills,
        "suggestions": suggestions,
        "ats_score": ats_score
    }