import streamlit as st
from resume_parser import parse_resume
from job_parser import parse_job_description
from similarity import compute_similarity
from skills import extract_skills
from gap_analysis import find_missing_skills, suggest_skills
from scorer import compute_skill_score, compute_final_score, interpret_score

st.set_page_config(page_title="Smart Resume Analyzer", page_icon="🚀", layout="wide")
st.title("Smart Resume Analyzer 🚀")
st.markdown("Analyze your resume against a job description and get AI-powered insights!")

# Upload Resume and Job Description
resume_file = st.file_uploader("Upload your Resume (.txt or .pdf)", type=["txt", "pdf"])
job_file = st.file_uploader("Upload Job Description (.txt)", type=["txt"])

if resume_file and job_file:
    # Save uploaded files temporarily
    resume_path = "temp_resume"
    job_path = "temp_job.txt"

    with open(resume_path, "wb") as f:
        f.write(resume_file.getbuffer())
    with open(job_path, "wb") as f:
        f.write(job_file.getbuffer())

    # Parse files
    resume_text = parse_resume(resume_path)
    job_text = parse_job_description(job_path)

    # Check if PDF extraction failed
    if resume_file.name.lower().endswith(".pdf") and len(resume_text.strip()) < 20:
        st.warning(
            "⚠️ It seems the PDF text could not be extracted properly. "
            "Please try uploading a TXT version of your resume for best results."
        )
    else:
        # Compute similarity and skills
        similarity_score = compute_similarity(resume_text, job_text)
        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_text)
        missing_skills = find_missing_skills(resume_skills, job_skills)
        skill_score = compute_skill_score(resume_skills, job_skills)
        final_score = compute_final_score(similarity_score, skill_score)
        verdict = interpret_score(final_score)
        skill_suggestions = suggest_skills(missing_skills)

        # --- Layout ---
        st.subheader("📊 Match Metrics")
        col1, col2, col3 = st.columns(3)

        # Text Similarity
        with col1:
            st.metric("Text Similarity", f"{similarity_score}%", delta_color="off")
            st.progress(similarity_score / 100)

        # Skill Match
        with col2:
            st.metric("Skill Match", f"{skill_score}%", delta_color="off")
            st.progress(skill_score / 100)

        # Final Score
        with col3:
            st.metric("Final Match Score", f"{final_score}%", delta_color="off")
            st.progress(final_score / 100)

        # Verdict Card
        color = "green" if final_score >= 70 else "orange" if final_score >= 40 else "red"
        st.markdown(f"<h3 style='color:{color}'>Verdict: {verdict}</h3>", unsafe_allow_html=True)

        # Skills Section
        st.subheader("💡 Skills Analysis")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Resume Skills:**")
            st.write(", ".join(sorted(resume_skills)) if resume_skills else "None")
        with col2:
            st.write("**Job Skills:**")
            st.write(", ".join(sorted(job_skills)) if job_skills else "None")

        # Missing Skills
        st.subheader("⚠️ Missing Skills")
        if missing_skills:
            for skill in missing_skills:
                link = skill_suggestions.get(skill, "No resource available")
                st.markdown(f"- **{skill}**: [Learn here]({link})")
        else:
            st.write("None! Great match! 🎉")
