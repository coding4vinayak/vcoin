from flask import Flask, render_template, request
from summarizer.text_summarizer import summarize_text
from summarizer.audio_summarizer import summarize_audio
from summarizer.image_summarizer import summarize_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text_summarization', methods=['GET', 'POST'])
def text_summarization():
    summary = None
    if request.method == 'POST':
        text = request.form['text']
        summary = summarize_text(text)
    return render_template('text_summarization.html', summary=summary)

@app.route('/audio_summarization', methods=['GET', 'POST'])
def audio_summarization():
    summary = None
    if request.method == 'POST':
        audio_file = request.files['audio']
        summary = summarize_audio(audio_file)
    return render_template('audio_summarization.html', summary=summary)

@app.route('/image_summarization', methods=['GET', 'POST'])
def image_summarization():
    summary = None
    if request.method == 'POST':
        image_file = request.files['image']
        summary = summarize_image(image_file)
    return render_template('image_summarization.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
