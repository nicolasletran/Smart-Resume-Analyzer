def resume_recommendations(resume_skills, job_skills):
    suggestions = []

    missing = job_skills - resume_skills
    if missing:
        suggestions.append(
            f"Consider adding experience or projects involving: {', '.join(missing)}"
        )

    if "python" in job_skills and "python" in resume_skills:
        suggestions.append(
            "Mention Python libraries (NumPy, Pandas, Scikit-learn) to strengthen technical depth."
        )

    if "machine learning" in job_skills and "machine learning" not in resume_skills:
        suggestions.append(
            "The job emphasizes Machine Learning — consider adding relevant coursework or projects."
        )

    if not suggestions:
        suggestions.append("Your resume aligns well with the job requirements!")

    return suggestions
