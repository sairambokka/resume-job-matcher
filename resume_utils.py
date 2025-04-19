import fitz
from sklearn.feature_extraction.text import CountVectorizer

def extract_text_from_pdf(file_stream):
    text = ""
    with fitz.open(stream=file_stream.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_keywords(text, max_keywords=15):
    vectorizer = CountVectorizer(max_features=max_keywords, stop_words="english")
    X = vectorizer.fit_transform([text])
    return vectorizer.get_feature_names_out()
