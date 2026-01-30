# Smart Resume Analyzer 🚀

**Smart Resume Analyzer** is an AI-powered tool that analyzes your resume against a job description, providing:

- **Text similarity** between resume and job description
- **Skill match score**
- **Final match score** with verdict (Low / Moderate / High)
- **Missing skills** with clickable learning resources

Built with **Python**, **Streamlit**, and **Sentence Transformers**.

---

## **Features**

- Upload **TXT or PDF resume** and **job description**  
- Semantic text similarity using **BERT embeddings**  
- Skill extraction and gap analysis  
- Suggested resources for missing skills  
- Clean, interactive **Streamlit UI**  

---

## **Getting Started**

### **Requirements**

Python 3.10+  
Install required packages:

```bash
pip install -r requirements.txt
```
Run the App Locally
```bash
streamlit run app.py
```
Open the browser at http://localhost:8501

Usage

Upload your resume (.txt recommended)

Upload a job description (.txt)

View:

Text similarity score

Skill match score

Final score & verdict

Missing skills & suggested resources

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
├─ requirements.txt
└─ data/
    ├─ sample_resume.txt
    └─ sample_job.txt
Notes

PDF resumes may not extract correctly if generated from Google Docs; TXT is recommended

For best results, use well-formatted resumes
