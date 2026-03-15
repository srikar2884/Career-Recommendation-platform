jobs = [

{"role":"Machine Learning Engineer",
 "skills":["python","machine learning","tensorflow","pandas"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=machine+learning+engineer"},

{"role":"Data Scientist",
 "skills":["python","machine learning","pandas","numpy"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=data+scientist"},

{"role":"Data Analyst",
 "skills":["python","sql","pandas","excel"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=data+analyst"},

{"role":"AI Engineer",
 "skills":["python","machine learning","deep learning"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=ai+engineer"},

{"role":"NLP Engineer",
 "skills":["python","nlp","machine learning"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=nlp+engineer"},

{"role":"Backend Developer",
 "skills":["java","spring","sql"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=backend+developer"},

{"role":"Frontend Developer",
 "skills":["javascript","react","html","css"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=frontend+developer"},

{"role":"Full Stack Developer",
 "skills":["javascript","react","node","mongodb"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=full+stack+developer"},

{"role":"Python Developer",
 "skills":["python","django","flask"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=python+developer"},

{"role":"Java Developer",
 "skills":["java","spring","microservices"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=java+developer"},

{"role":"Cloud Engineer",
 "skills":["aws","docker","kubernetes"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=cloud+engineer"},

{"role":"AWS Cloud Architect",
 "skills":["aws","cloud","architecture"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=aws+cloud+architect"},

{"role":"DevOps Engineer",
 "skills":["docker","kubernetes","ci/cd","git"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=devops+engineer"},

{"role":"Site Reliability Engineer",
 "skills":["linux","cloud","docker"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=site+reliability+engineer"},

{"role":"Cyber Security Analyst",
 "skills":["networking","linux","security"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=cyber+security+analyst"},

{"role":"Penetration Tester",
 "skills":["security","penetration testing","linux"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=penetration+tester"},

{"role":"Network Engineer",
 "skills":["networking","routing","switching"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=network+engineer"},

{"role":"Mobile App Developer",
 "skills":["java","android","kotlin"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=android+developer"},

{"role":"iOS Developer",
 "skills":["swift","ios","mobile"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=ios+developer"},

{"role":"Software Engineer",
 "skills":["java","python","software development"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=software+engineer"},

{"role":"Software Development Engineer",
 "skills":["python","java","algorithms"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=software+development+engineer"},

{"role":"Database Administrator",
 "skills":["sql","database","mysql"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=database+administrator"},

{"role":"Data Engineer",
 "skills":["python","sql","data pipelines"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=data+engineer"},

{"role":"Business Intelligence Analyst",
 "skills":["sql","data analysis","power bi"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=business+intelligence+analyst"},

{"role":"Product Analyst",
 "skills":["sql","data analysis","analytics"],
 "link":"https://www.linkedin.com/jobs/search/?keywords=product+analyst"}

]


def get_recommended_jobs(user_skills):

    results = []

    for job in jobs:

        match = set(user_skills).intersection(set(job["skills"]))

        score = (len(match) / len(job["skills"])) * 100

        if score >= 50:   # only jobs with 50% match

            results.append({
                "role": job["role"],
                "link": job["link"],
                "score": round(score,2)
            })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results
#--------------ALL JOBS------------------------
def get_all_jobs_with_match(user_skills):

    results = []

    for job in jobs:

        match = set(user_skills).intersection(set(job["skills"]))

        score = (len(match) / len(job["skills"])) * 100

        results.append({
            "role": job["role"],
            "link": job["link"],
            "score": round(score,2)
        })

    # sort by match %
    results.sort(key=lambda x: x["score"], reverse=True)

    return results