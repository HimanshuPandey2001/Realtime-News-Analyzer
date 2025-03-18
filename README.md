---
title: Real-Time News Analyzer
emoji: 📰
colorFrom: blue
colorTo: purple
sdk: docker
sdk_version: "1.32.0"
app_file: app.py
pinned: false
---

# Real-Time News Analyzer

A web application that analyzes news articles for sentiment and generates Hindi audio summaries using AI.

## Features
- Fetches real-time news via GNews API
- Sentiment Analysis (Positive/Negative/Neutral)
- Hindi Text-to-Speech (TTS)
- Topic Extraction using NLP
- Interactive Streamlit UI

## Setup
1. Get API key from [GNews.io](https://gnews.io)
2. Add key to Hugging Face Space secrets
3. App will auto-deploy!

## Usage
1. Enter company name (e.g., "Reliance" or "Tesla")
2. Click "Analyze" to get:
   - News articles with sentiment
   - Key topics
   - Hindi audio summary

[![Deploy to Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Deploy%20to-Hugging%20Face-blue)](https://huggingface.co/spaces/himanshu200113/Realtimenews)

> **Note**: First build may take 5-7 minutes