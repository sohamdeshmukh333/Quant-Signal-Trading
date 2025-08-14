# src/api/sentiment.py

from fastapi import APIRouter, Query
from src.services.sentiment_analysis import scrape_tweets, analyze_sentiment

router = APIRouter()

@router.get("/sentiment")
def get_sentiment(symbol: str = Query(..., description="Stock symbol like AAPL or TSLA"), limit: int = 100):
    try:
        tweets = scrape_tweets(symbol, limit)
        result = analyze_sentiment(tweets)
        return result
    except Exception as e:
        return {"error": str(e)}
