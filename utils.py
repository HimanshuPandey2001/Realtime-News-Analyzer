import os
import io
from transformers import pipeline
from rake_nltk import Rake
from collections import defaultdict
from gtts import gTTS
import nltk

# Configure cache directories
os.environ['HF_HOME'] = '/tmp/cache/huggingface'
os.environ['NLTK_DATA'] = '/tmp/cache/nltk'

# Initialize models
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    framework="pt"
)
r = Rake()

# Download NLTK data
nltk.download('punkt', download_dir=os.environ['NLTK_DATA'])
nltk.download('stopwords', download_dir=os.environ['NLTK_DATA'])

def analyze_sentiment(text):
    try:
        result = sentiment_analyzer(text[:512])[0]
        return result['label'].capitalize()
    except:
        return "Neutral"

def extract_topics(text):
    try:
        r.extract_keywords_from_text(text)
        return [phrase.capitalize() for phrase, _ in r.get_ranked_phrases_with_scores()[:3]]
    except:
        return []

def generate_tts(text):
    try:
        tts = gTTS(text=text, lang='hi')
        audio_bytes = io.BytesIO()
        tts.write_to_fp(audio_bytes)
        return audio_bytes.getvalue()
    except:
        return b""