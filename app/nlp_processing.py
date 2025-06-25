# nlp_processing.py
from transformers import pipeline
import spacy

nlp = spacy.load("en_core_web_sm")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_words=150):
    summary = summarizer(text, max_length=max_words, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def extract_concepts(summary_text):
    doc = nlp(summary_text)
    concepts = [chunk.text for chunk in doc.noun_chunks if len(chunk.text.split()) <= 5]
    return concepts

def generate_mermaid_code(concepts):
    mermaid_lines = ["graph TD"]
    for i, concept in enumerate(concepts):
        if i < len(concepts) - 1:
            mermaid_lines.append(f"    A{i}[{concept}] --> A{i+1}[{concepts[i+1]}]")
        else:
            mermaid_lines.append(f"    A{i}[{concept}]")
    return "\n".join(mermaid_lines)

