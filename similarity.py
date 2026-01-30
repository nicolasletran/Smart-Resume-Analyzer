from sentence_transformers import SentenceTransformer, util

# Load a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')  # small, fast, good for our use case

def compute_similarity(resume_text: str, job_text: str) -> float:
    """
    Computes semantic similarity between resume and job description
    Returns similarity as a percentage
    """
    # Embed the texts
    embeddings_resume = model.encode(resume_text, convert_to_tensor=True)
    embeddings_job = model.encode(job_text, convert_to_tensor=True)
    
    # Compute cosine similarity
    similarity_score = util.cos_sim(embeddings_resume, embeddings_job).item()
    
    # Convert to percentage
    return round(similarity_score * 100, 2)
