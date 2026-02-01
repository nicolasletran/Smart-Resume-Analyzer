import os
import re
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from fpdf import FPDF
from resume_parser import parse_resume
from job_parser import parse_job_description
from similarity import compute_similarity
from skills import extract_skills
from gap_analysis import find_missing_skills, suggest_skills
from scorer import compute_skill_score, compute_final_score, interpret_score, score_breakdown
from recommendations import resume_recommendations

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Smart Resume Analyzer", page_icon="🚀", layout="wide")
st.title("Smart Resume Analyzer 🚀")
st.markdown("Analyze how well your resume matches a job description using AI and get improvement suggestions.")

# ---- DEMO MODE ----
demo_mode = st.checkbox("Use demo data (recommended)", value=False)

if demo_mode:
    resume_text = open("data/sample_resume.txt", encoding="utf-8").read()
    job_text = open("data/sample_job.txt", encoding="utf-8").read()
else:
    resume_file = st.file_uploader("Upload Resume (.txt, .pdf, .docx)", type=["txt", "pdf", "docx"])
    job_file = st.file_uploader("Upload Job Description (.txt, .pdf, .docx)", type=["txt", "pdf", "docx"])

    if not resume_file or not job_file:
        st.stop()

    # Save uploaded files
    resume_ext = os.path.splitext(resume_file.name)[1]
    job_ext = os.path.splitext(job_file.name)[1]

    temp_resume_path = f"temp_resume{resume_ext}"
    temp_job_path = f"temp_job{job_ext}"

    with open(temp_resume_path, "wb") as f:
        f.write(resume_file.getbuffer())
    with open(temp_job_path, "wb") as f:
        f.write(job_file.getbuffer())

    # Parse files
    resume_text = parse_resume(temp_resume_path)
    job_text = parse_job_description(temp_job_path)

# ---- ANALYSIS ----
similarity_score = compute_similarity(resume_text, job_text)
resume_skills = extract_skills(resume_text)
job_skills = extract_skills(job_text)
missing_skills = find_missing_skills(resume_skills, job_skills)

skill_score = compute_skill_score(resume_skills, job_skills)
final_score = compute_final_score(similarity_score, skill_score)
verdict = interpret_score(final_score)

# ---- METRICS ----
st.subheader("📊 Match Overview")
c1, c2, c3 = st.columns(3)

c1.metric("Text Similarity", f"{similarity_score:.1f}%")
c1.progress(similarity_score / 100)

c2.metric("Skill Match", f"{skill_score:.1f}%")
c2.progress(skill_score / 100)

c3.metric("Final Score", f"{final_score:.1f}%")
c3.progress(final_score / 100)

st.markdown(f"### Verdict: **{verdict}**")

# ---- EXPLAINABILITY ----
st.subheader("🔍 How the Score Was Calculated")
with st.expander("Click to see breakdown"):
    breakdown = score_breakdown(similarity_score, skill_score)
    for k, v in breakdown.items():
        st.write(f"**{k}:** {v}")

# ---- RADAR CHART ----
st.subheader("📈 Skill Coverage Radar Chart")
all_skills = list(job_skills.union(resume_skills))
resume_values = [1 if skill in resume_skills else 0 for skill in all_skills]
job_values = [1 for _ in all_skills]

fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=job_values, theta=all_skills, fill='toself', name='Job Required'))
fig.add_trace(go.Scatterpolar(r=resume_values, theta=all_skills, fill='toself', name='Your Resume'))
fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,1])), showlegend=True)
st.plotly_chart(fig)

# ---- SKILL GAP ----
st.subheader("⚠️ Skill Gap & Learning Plan")
suggestions = suggest_skills(missing_skills)
if missing_skills:
    for skill, link in suggestions.items():
        st.markdown(f"- **{skill}** → [Learn here]({link})")
else:
    st.success("No missing skills! Great alignment 🎉")

# ---- RESUME IMPROVEMENTS ----
st.subheader("🛠 Resume Improvement Suggestions")
tips = resume_recommendations(resume_skills, job_skills)
for tip in tips:
    st.write(f"• {tip}")

# ---- PDF REPORT DOWNLOAD ----
st.subheader("💾 Download Report")

def generate_pdf():
    pdf = FPDF()
    pdf.add_page()

    # Add Unicode font (DejaVu)
    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', '', 16)

    # Safe title (remove unsupported characters)
    safe_title = re.sub(r'[^\x00-\xFF]', '', "Smart Resume Analyzer Report 🚀")
    pdf.cell(0, 10, safe_title, ln=True, align="C")

    pdf.set_font('DejaVu', '', 12)
    pdf.ln(10)
    pdf.cell(0, 8, f"Text Similarity: {similarity_score:.1f}%", ln=True)
    pdf.cell(0, 8, f"Skill Match: {skill_score:.1f}%", ln=True)
    pdf.cell(0, 8, f"Final Score: {final_score:.1f}%", ln=True)
    pdf.cell(0, 8, f"Verdict: {verdict}", ln=True)
    pdf.ln(5)

    pdf.set_font('DejaVu', '', 14)
    pdf.cell(0, 8, "Skill Gap & Learning Plan:", ln=True)
    pdf.set_font('DejaVu', '', 12)
    if missing_skills:
        for skill, link in suggestions.items():
            pdf.multi_cell(0, 6, f"- {skill} → {link}")
    else:
        pdf.cell(0, 6, "No missing skills! Great alignment 🎉", ln=True)

    pdf.ln(5)
    pdf.set_font('DejaVu', '', 14)
    pdf.cell(0, 8, "Resume Improvement Tips:", ln=True)
    pdf.set_font('DejaVu', '', 12)
    for tip in tips:
        pdf.multi_cell(0, 6, f"- {tip}")

    pdf_file = "resume_report.pdf"
    pdf.output(pdf_file)
    return pdf_file

if st.button("Download PDF Report"):
    report_file = generate_pdf()
    with open(report_file, "rb") as f:
        st.download_button(
            "Click to Download Report",
            f,
            file_name="resume_report.pdf",
            mime="application/pdf"
        )
