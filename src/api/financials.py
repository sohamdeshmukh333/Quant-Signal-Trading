from fastapi import APIRouter, Query
from src.services.yahoo import get_financials

router = APIRouter()
@router.get("/financials")
def get_financial_data(symbol: str = Query(..., description="Stock symbol like AAPL or TSLA")):
    return get_financials(symbol)

