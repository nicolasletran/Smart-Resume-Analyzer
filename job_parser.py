import re
import nltk
from nltk.corpus import stopwords

# Download stopwords if not already
nltk.download('stopwords')
STOP_WORDS = set(stopwords.words('english'))

def clean_text(text: str) -> str:
    """
    Lowercase, remove non-alphabetic characters, remove stopwords
    """
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in STOP_WORDS]
    return ' '.join(words)

def parse_job_description(file_path: str) -> str:
    """
    Parses a job description from a .txt file
    """
    # Try UTF-8, fallback to latin1 for non-UTF8 files
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin1') as file:
            text = file.read()

    return clean_text(text)
