import torchaudio
from transformers import pipeline
from summarizer.text_summarizer import summarize_text

# Initialize the speech-to-text pipeline
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-large")

def summarize_audio(audio_file):
    waveform, sample_rate = torchaudio.load(audio_file)
    audio_text = transcriber(audio_file)["text"]
    return summarize_text(audio_text)
