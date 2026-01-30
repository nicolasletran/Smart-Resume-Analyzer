import re
import nltk
import pdfplumber
from nltk.corpus import stopwords

nltk.download('stopwords')
STOP_WORDS = set(stopwords.words('english'))

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in STOP_WORDS]
    return ' '.join(words)

def parse_resume(file_path: str) -> str:
    """
    Parses a resume from .txt or .pdf
    """
    if file_path.lower().endswith('.pdf'):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
    else:
        # TXT files: try UTF-8 first, fallback to latin1
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='latin1') as f:
                text = f.read()
    return clean_text(text)
