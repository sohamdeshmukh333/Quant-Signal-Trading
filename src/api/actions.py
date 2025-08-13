#src/api/actions.py
from fastapi import APIRouter, Query
from src.services.yahoo import get_actions

router = APIRouter()
@router.get("/actions")
def get_action_data(symbol: str = Query(..., description="Stock symbol like AAPL or TSLA")):
    return get_actions(symbol)