#src/api/prices.py
from fastapi import APIRouter, Query
from typing import Optional #so parameters like start, end can be optional
from src.services.yahoo import fetch_prices #actual logic written in yahoo.py

router = APIRouter() #define routes seperately and "plug them in" later

@router.get("/prices")
def get_prices(symbol: str= Query(...,description="Stock sybmol like AAPL or TSLA"),
               start: Optional[str] = None,
               end: Optional[str] = None,
               interval: str = "1d",
               period: str = "1y", 
               adjusted: bool = True
               ):
    
    return fetch_prices(symbol, start,end, interval, period, adjusted)
    
