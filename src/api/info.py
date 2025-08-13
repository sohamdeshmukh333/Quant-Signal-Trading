from fastapi import APIRouter, Query
from src.services.yahoo import get_company_info

router = APIRouter()
@router.get("/info")
def get_info(symbol: str = Query(..., description="Stock symbol like AAPL or TSLA")):
    return get_company_info(symbol)



