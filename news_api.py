import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_news(company, max_articles=10):
    """Fetch news from GNews API"""
    api_key = os.getenv("GNEWS_API_KEY")
    url = f"https://gnews.io/api/v4/search?q={company}&max={max_articles}&apikey={api_key}"
    
    try:
        response = requests.get(url)
        return response.json().get('articles', [])[:max_articles]
    except Exception as e:
        print(f"News API Error: {str(e)}")
        return []