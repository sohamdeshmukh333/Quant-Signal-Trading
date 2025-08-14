# src/services/sentiment_analysis.py

import snscrape.modules.twitter as sntwitter
from typing import List
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load FinBERT model + tokenizer
try:
    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
    model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
    model.eval()
except Exception as e:
    print(f"Model load error: {e}")
    tokenizer = None
    model = None

def scrape_tweets(symbol: str, limit: int = 100) -> List[str]:
    query = f"{symbol} stock since:2024-01-01"
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= limit:
            break
        tweets.append(tweet.content)
    return tweets

def analyze_sentiment(tweets: List[str]) -> dict:
    scores = {"positive": 0, "neutral": 0, "negative": 0}

    if not tokenizer or not model:
        return {"error": "Model failed to load."}

    try:
        for text in tweets:
            inputs = tokenizer(text, return_tensors="pt", truncation=True)
            with torch.no_grad():
                outputs = model(**inputs)
                logits = outputs.logits
                probs = torch.nn.functional.softmax(logits, dim=1)[0].numpy()

            scores["positive"] += probs[0]
            scores["negative"] += probs[1]
            scores["neutral"]  += probs[2]

        total = len(tweets)
        if total > 0:
            for k in scores:
                scores[k] = round(scores[k] / total, 4)

        return scores
    
    except Exception as e:
        print(f"Sentiment analysis error: {e}")
        return {"error": str(e)}
