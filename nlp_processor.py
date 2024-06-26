import PyPDF2
import docx
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import os

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

def extract_text(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == '.pdf':
        return extract_text_from_pdf(file_path)
    elif file_extension.lower() == '.docx':
        return extract_text_from_docx(file_path)
    elif file_extension.lower() == '.txt':
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        raise ValueError("Unsupported file format")

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return " ".join([paragraph.text for paragraph in doc.paragraphs])

def analyze_text(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    
    word_freq = Counter(filtered_words)
    
    key_phrases = [" ".join(filtered_words[i:i+3]) for i in range(len(filtered_words)-2)]
    phrase_freq = Counter(key_phrases)
    
    return {
        'word_count': len(words),
        'sentence_count': len(sentences),
        'top_words': dict(word_freq.most_common(10)),
        'top_phrases': dict(phrase_freq.most_common(5))
    }

def process_files(file_paths):
    results = []
    for file_path in file_paths:
        text = extract_text(file_path)
        analysis = analyze_text(text)
        results.append({
            'filename': os.path.basename(file_path),
            'analysis': analysis
        })
    return results