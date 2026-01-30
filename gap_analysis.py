def find_missing_skills(resume_skills: set, job_skills: set) -> set:
    """
    Returns a set of skills required by the job that are missing in the resume
    """
    return job_skills - resume_skills
# Optional mapping of skills to resources
SKILL_RESOURCES = {
    "python": "https://www.learnpython.org/",
    "c": "https://www.learn-c.org/",
    "sql": "https://www.w3schools.com/sql/",
    "linux": "https://linuxjourney.com/",
    "git": "https://git-scm.com/book/en/v2",
    "machine learning": "https://www.coursera.org/learn/machine-learning",
    "docker": "https://www.docker.com/get-started",
    "data analysis": "https://www.datacamp.com/courses/data-analysis-with-python"
}

def suggest_skills(missing_skills: set) -> dict:
    """
    Returns a dictionary of missing skills mapped to learning resources
    """
    suggestions = {}
    for skill in missing_skills:
        suggestions[skill] = SKILL_RESOURCES.get(skill, "No resource available")
    return suggestions
