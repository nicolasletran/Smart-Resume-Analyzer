from resume_parser import parse_resume
from job_parser import parse_job_description
from similarity import compute_similarity
from skills import extract_skills
from gap_analysis import find_missing_skills, suggest_skills
from scorer import compute_skill_score, compute_final_score, interpret_score

# Change these paths to your test files
resume_file = "data/sample_resume.pdf"   # or .txt
job_file = "data/sample_job.txt"

# Parse files
resume_text = parse_resume(resume_file)
job_text = parse_job_description(job_file)

# Compute similarity
similarity_score = compute_similarity(resume_text, job_text)

# Extract skills
resume_skills = extract_skills(resume_text)
job_skills = extract_skills(job_text)
missing_skills = find_missing_skills(resume_skills, job_skills)

# Skill scores
skill_score = compute_skill_score(resume_skills, job_skills)
final_score = compute_final_score(similarity_score, skill_score)

# Display results
print("===== Smart Resume Analyzer Results =====")
print(f"Text Similarity Score: {similarity_score}%")
print(f"Skill Match Score: {skill_score}%")
print(f"Final Match Score: {final_score}%")
print(f"Verdict: {interpret_score(final_score)}")
print(f"Resume Skills: {resume_skills}")
print(f"Job Skills: {job_skills}")
print(f"Missing Skills: {missing_skills}")

# Suggested skills
skill_suggestions = suggest_skills(missing_skills)
if skill_suggestions:
    print("\nSuggested Skills to Learn 🎯")
    for skill, link in skill_suggestions.items():
        print(f"- {skill}: {link}")
