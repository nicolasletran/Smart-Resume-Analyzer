import re
import nltk
import pdfplumber
import docx
import pytesseract
from pdf2image import convert_from_path
from nltk.corpus import stopwords
from PIL import Image

# Download stopwords
nltk.download('stopwords')
STOP_WORDS = set(stopwords.words('english'))

def clean_text(text: str) -> str:
    """
    Cleans text by:
    - Lowercasing
    - Removing non-alphabetic characters
    - Removing stopwords
    - Removing extra whitespace
    """
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    words = text.split()
    words = [w for w in words if w not in STOP_WORDS]
    return ' '.join(words)

def parse_resume(file_path: str) -> str:
    """
    Parses a resume from .txt, .pdf, or .docx
    """
    import os

    ext = os.path.splitext(file_path)[1].lower()

    text = ""

    if ext == '.pdf':
        try:
            import pdfplumber
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + " "
        except Exception as e:
            # fallback to OCR for scanned PDFs or weird PDFs
            from pdf2image import convert_from_path
            import pytesseract
            pages = convert_from_path(file_path)
            for page in pages:
                text += pytesseract.image_to_string(page) + " "
    elif ext == '.docx':
        from docx import Document
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + " "
    elif ext == '.txt':
        # TXT files: try UTF-8 first, fallback to latin1
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='latin1') as f:
                text = f.read()
    else:
        raise ValueError("Unsupported file type. Only .txt, .pdf, .docx allowed.")

    return clean_text(text)

