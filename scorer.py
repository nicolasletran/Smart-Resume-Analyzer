def compute_skill_score(resume_skills, job_skills):
    if not job_skills:
        return 100.0
    matched = resume_skills.intersection(job_skills)
    return round((len(matched) / len(job_skills)) * 100, 2)


def compute_final_score(text_similarity, skill_score):
    # Weight skills more heavily (real-world logic)
    return round((0.4 * text_similarity) + (0.6 * skill_score), 2)


def interpret_score(score):
    if score >= 70:
        return "High match ✅"
    elif score >= 40:
        return "Moderate match ⚠️"
    else:
        return "Low match ❌"


def score_breakdown(text_similarity, skill_score):
    return {
        "Text Similarity Weight": "40%",
        "Skill Match Weight": "60%",
        "Text Similarity Score": text_similarity,
        "Skill Match Score": skill_score
    }
