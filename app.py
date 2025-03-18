import streamlit as st
from news_api import fetch_news
from utils import analyze_sentiment, extract_topics, generate_tts
import base64

st.set_page_config(page_title="News Analyzer", layout="wide")
st.title("📰 Real-Time News Analysis")

# Input Section
company = st.text_input("Enter Company Name", "Reliance")

if st.button("Analyze"):
    with st.spinner("Processing News Articles..."):
        try:
            articles = fetch_news(company)
            
            if not articles:
                st.warning("No articles found. Try another company name.")
            else:
                processed = []
                for article in articles:
                    processed.append({
                        "title": article.get('title', 'No Title'),
                        "summary": article.get('description', 'No Summary')[:200] + "...",
                        "sentiment": analyze_sentiment(article.get('content', '')),
                        "topics": extract_topics(article.get('content', ''))
                    })
                
                # Display Results
                st.subheader(f"Analysis Report for {company}")
                
                # Articles Display
                with st.expander(f"View {len(processed)} Articles"):
                    for idx, art in enumerate(processed, 1):
                        st.markdown(f"**Article {idx}: {art['title']}**")
                        st.caption(f"Sentiment: {art['sentiment']}")
                        st.write(art['summary'])
                        st.write(f"**Topics**: {', '.join(art['topics'])}")
                        st.divider()
                
                # Audio Summary
                summary = f"{company} के {len(processed)} समाचार लेख मिले। सकारात्मक: {len([a for a in processed if a['sentiment'] == 'Positive'])} | नकारात्मक: {len([a for a in processed if a['sentiment'] == 'Negative'])}"
                audio = generate_tts(summary)
                if audio:
                    st.audio(audio, format="audio/wav")
                
        except Exception as e:
            st.error(f"Analysis failed: {str(e)}")