# Smart Resume Analyzer 🚀

**Smart Resume Analyzer** is an AI-powered tool that evaluates your resume against a job description, providing actionable insights to help you improve your job applications.

It helps you:  

- Compare **text similarity** between your resume and the job description  
- Calculate **skill match score**  
- Generate a **final match score** with an easy-to-read verdict (Low / Moderate / High)  
- Identify **missing skills** and provide clickable **learning resources**  
- Suggest **resume improvements** based on skill gaps  
- Visualize **skill coverage** in an interactive radar chart  
- Download a **PDF report** summarizing the analysis  

Built with **Python**, **Streamlit**, **BERT embeddings**, and **FPDF**.

---

## Features

- Upload **.txt, .pdf, or .docx** resumes and job descriptions  
- Semantic text similarity using **Sentence Transformers**  
- Extract and analyze skills using NLP  
- Provide learning resources for missing skills  
- Interactive **Streamlit dashboard** with charts and explanations  
- Generate a **PDF report** of your analysis  
- Resume improvement suggestions to optimize alignment with job requirements  

---

## Getting Started

### Requirements

- Python 3.10+  
- Install required packages:

```bash
pip install -r requirements.txt
```
Run the App Locally
```bash
streamlit run app.py
```
Open the browser at http://localhost:8501

Usage

Usage:

Upload your resume (.txt recommended, also supports .pdf and .docx)

Upload a job description (.txt recommended, also supports .pdf and .docx)

View results:

Text similarity score

Skill match score

Final score & verdict

Missing skills & suggested learning resources

Radar chart showing skill coverage

Resume improvement suggestions

Optionally, download a PDF report of your results

Folder Structure:
Smart-Resume-Analyzer/
├─ app.py
├─ main.py
├─ resume_parser.py
├─ job_parser.py
├─ similarity.py
├─ skills.py
├─ gap_analysis.py
├─ scorer.py
├─ recommendations.py
├─ requirements.txt
└─ data/
    ├─ sample_resume.txt
    └─ sample_job.txt


PDF resumes may not extract correctly if generated from Google Docs; TXT is recommended

For best results, use well-formatted resumes
