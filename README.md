# 🧠 Quant AI Signal Discovery

A full-stack project that uses **AI/NLP models** to discover alpha signals from **alternative data sources** (like Twitter or Reddit) and backtests their predictive power on real stock market data. Built entirely from scratch using Python and deployed on AWS.

---

## 📈 Project Goal

To build an end-to-end quant research pipeline that:

- Scrapes and processes social media data (e.g. tweets about SPY)
- Uses NLP to extract sentiment and generate trading signals
- Merges these signals with historical stock data
- Trains machine learning models to predict next-day price movement
- Backtests a simple trading strategy using those signals
- Deploys a live Streamlit dashboard on AWS

---

## 🚀 Features

- 🐦 **Twitter scraping** using `snscrape`
- 🤖 **Sentiment scoring** with FinBERT (`transformers`)
- 📊 **Historical price integration** with `yfinance`
- 🧠 **ML modeling** (RandomForest, XGBoost) for signal prediction
- 💸 **Backtesting** and Sharpe ratio calculation
- 🌐 **Interactive dashboard** built with Streamlit
- ☁️ **Deployment-ready** via AWS EC2 or Elastic Beanstalk

---

## 🧱 Tech Stack

| Tool | Usage |
|------|-------|
| Python | Core language |
| snscrape | Tweet scraping |
| transformers | FinBERT sentiment analysis |
| yfinance | Stock price data |
| scikit-learn, XGBoost | Machine learning |
| pandas, matplotlib | Data manipulation & plotting |
| Streamlit | Frontend dashboard |
| AWS (EC2/S3) | Deployment and storage |


## 📂 Folder Structure

