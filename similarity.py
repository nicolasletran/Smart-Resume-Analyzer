from sentence_transformers import SentenceTransformer, util

# Load Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(resume_text: str, job_text: str) -> float:
    """
    Computes similarity between resume text and job description text.
    Returns a percentage (0-100).
    """
    if not resume_text or not job_text:
        return 0.0

    # Convert texts to embeddings
    resume_emb = model.encode(resume_text, convert_to_tensor=True)
    job_emb = model.encode(job_text, convert_to_tensor=True)

    # Cosine similarity
    similarity_score = util.cos_sim(resume_emb, job_emb).item() * 100
    return round(similarity_score, 2)
