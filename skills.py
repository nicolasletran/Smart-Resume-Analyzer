import re

# Example skill list (expandable)
SKILL_LIST = [
    "python", "c", "c++", "java", "javascript", "sql", "linux", "git",
    "machine learning", "data analysis", "deep learning", "docker",
    "kubernetes", "react", "angular", "nodejs", "aws", "azure", "gcp"
]

# Map common synonyms to standard names
SKILL_SYNONYMS = {
    "ml": "machine learning",
    "ai": "machine learning",
    "js": "javascript",
    "py": "python",
    "data analytics": "data analysis"
}

def extract_skills(text: str) -> set:
    """
    Extracts skills from text.
    Normalizes synonyms to standard names.
    """
    text = text.lower()
    found_skills = set()

    for skill in SKILL_LIST:
        # Check if skill or synonym exists in text
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            found_skills.add(skill)

    # Map synonyms
    normalized_skills = set()
    for skill in found_skills:
        normalized_skills.add(SKILL_SYNONYMS.get(skill, skill))

    return normalized_skills
