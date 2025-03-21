FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y libsndfile1

# Create cache directories
RUN mkdir -p /tmp/cache/huggingface /tmp/cache/nltk && \
    chmod -R 777 /tmp/cache

# Set environment variables
ENV HF_HOME=/tmp/cache/huggingface \
    NLTK_DATA=/tmp/cache/nltk

WORKDIR /app
COPY . .

# Install Python dependencies with PyTorch CPU version
RUN pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt
RUN python -c "import nltk; nltk.download('punkt', download_dir='/tmp/cache/nltk'); nltk.download('stopwords', download_dir='/tmp/cache/nltk')"

CMD ["streamlit", "run", "app.py", "--server.port=7860"]