# src/services/yahoo.py
from __future__ import annotations
# This module fetches stock prices and financial data from Yahoo Finance using the yfinance library.

import yfinance as yf
import pandas as pd
from typing import List, Dict, Optional


ALLOWED_INTERVALS = {"1d", "1h", "30m", "15m", "5m", "1m"}

def fetch_prices(
    symbol: str,
    start: Optional[str] = None,   # "YYYY-MM-DD"
    end: Optional[str] = None,     # "YYYY-MM-DD"
    interval: str = "1d",          # bar size
    period: str = "1y",            # lookback if start/end not provided
    adjusted: bool = True          # auto-adjust for splits/divs
) -> List[Dict]:
    """
    Return list of dicts:
      - date (MM-DD-YYYY for daily; MM-DD-YYYY HH:MM:SS for intraday)
      - open, high, low, close (float)
      - volume (int)
    """
    symbol = str(symbol.strip().upper())
    if not symbol:
        return []

    if interval not in ALLOWED_INTERVALS:
        interval = "1d"  # default to daily if invalid

    #Create a ticker object
    tkr = yf.Ticker(symbol)

    #Fetch historical market data
    if start or end:
        df = tkr.history(start=start, end=end, interval=interval, auto_adjust=adjusted)
    else:
        df = tkr.history(period=period, interval=interval, auto_adjust=adjusted)
    
    if df.empty or df is None:
        return []

    df = df.rename(columns=str.lower)
    is_daily = interval == "1d"

    OHLCV_data: List[Dict] = []

    for idx, row in df.iterrows():
        timestamp = pd.Timestamp(idx)
        if timestamp.tzinfo is not None:
            timestamp = timestamp.tz_convert(None)

        date_str = (
            timestamp.strftime("%m-%d-%Y") if is_daily
            else timestamp.strftime("%m-%d-%Y %H:%M:%S")
        )
        
        row_data = row.to_dict()
        close_val = row_data.get('close', row_data.get('adj close'))
        vol_val = row_data.get("volume",0)

        OHLCV_data.append({
            "date": date_str,
            "open": float(row['open']),
            "high": float(row['high']),
            "low": float(row['low']),
            "close": float(close_val),
            "volume": int(vol_val) if pd.notna(vol_val) else 0
        })

    return OHLCV_data
        

# #Fetch basic financials
# financials = ticker.financials
# print(f"\nFinancials for {tickerSymbol}:")
# print(financials)

# #Fetch stock actions like dividends and splits
# actions = ticker.actions
# print("\nStock Actions:")
# print(actions)