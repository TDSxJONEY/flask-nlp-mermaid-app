# 🧠 Flask NLP Summarizer with Mermaid Diagram Generator

This project is a Flask-based web application that uses a transformer model (BART) to summarize text and then generates Mermaid diagram code to visualize the summary structure.

---

## 🚀 Features

- 📄 Accepts long-form text input
- 🤖 Uses Hugging Face’s `facebook/bart-large-cnn` model for summarization
- 🔁 Transforms summary into Mermaid.js diagram format
- 🧾 Allows users to copy Mermaid code and preview it externally
- 🐳 Docker-ready for easy deployment

---

## 🧱 Tech Stack

- **Frontend:** HTML, CSS (Jinja templates)
- **Backend:** Python, Flask
- **NLP Model:** HuggingFace Transformers (`facebook/bart-large-cnn`)
- **Visualization:** Mermaid.js syntax
- **Packaging:** Docker

---

## 🧪 Local Development Setup

```bash
# 1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # On Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python run.py
