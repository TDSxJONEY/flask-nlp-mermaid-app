from flask import Blueprint, render_template, request
from app.nlp_processing import summarize_text, extract_concepts, generate_mermaid_code

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    summary = ''
    mermaid_code = ''
    if request.method == 'POST':
        text = request.form['input_text']
        max_words = int(request.form['max_words'])
        summary = summarize_text(text, max_words=max_words)
        concepts = extract_concepts(summary)
        mermaid_code = generate_mermaid_code(concepts)
    return render_template('index.html', summary=summary, mermaid_code=mermaid_code)