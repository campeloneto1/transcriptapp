# summarizer.py

import spacy

# Certifique-se de instalar o modelo com:
# python -m spacy download pt_core_news_sm
nlp = spacy.load("pt_core_news_sm")

def summarize_text(text, max_sentences=5):
    doc = nlp(text)
    sentences = list(doc.sents)
    # Pega as primeiras frases bem formadas
    summary = " ".join(str(sent).strip() for sent in sentences[:max_sentences])
    return summary
