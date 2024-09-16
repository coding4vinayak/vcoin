# app.py
from flask import Flask, render_template, request
from summarizer import summarize_text  # Import the summarization function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    if request.method == 'POST':
        article_text = request.form.get('article_text')
        if article_text:
            summary = summarize_text(article_text)
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
