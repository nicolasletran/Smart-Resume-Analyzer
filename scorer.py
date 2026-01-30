def compute_skill_score(resume_skills: set, job_skills: set) -> float:
    """
    Returns skill match as a percentage
    """
    if not job_skills:
        return 100.0
    matched = resume_skills.intersection(job_skills)
    return round(len(matched) / len(job_skills) * 100, 2)

def compute_final_score(similarity_score: float, skill_score: float) -> float:
    """
    Returns a weighted final score: 70% text similarity, 30% skill match
    """
    return round(0.7 * similarity_score + 0.3 * skill_score, 2)

def interpret_score(score: float) -> str:
    """
    Returns a text verdict based on the final score
    """
    if score >= 75:
        return "Excellent match"
    elif score >= 50:
        return "Moderate match"
    else:
        return "Low match"
