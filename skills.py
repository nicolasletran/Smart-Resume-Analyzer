# List of important skills
SKILLS = [
    "python", "c", "sql", "linux", "git",
    "machine learning", "docker", "data analysis"
]

def extract_skills(text: str) -> set:
    """
    Returns a set of skills found in the text
    """
    found = set()
    for skill in SKILLS:
        if skill in text:
            found.add(skill)
    return found
