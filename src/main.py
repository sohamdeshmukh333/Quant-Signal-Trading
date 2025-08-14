from fastapi import FastAPI
from src.api import prices, info, actions, financials, sentiment

app = FastAPI()


app.include_router(prices.router, prefix="/api")
app.include_router(actions.router, prefix="/api")
app.include_router(financials.router, prefix="/api")
app.include_router(info.router, prefix="/api")
app.include_router(sentiment.router, prefix="/api")
#Root route
@app.get("/")
async def root():
    return {"message": "Hello, World!"}



#http://localhost:8000/api/prices?symbol=AAPL
#http://localhost:8000/api/info?symbol=AAPL
#http://localhost:8000/api/actions?symbol=AAPL
#http://localhost:8000/api/financials?symbol=AAPL
#http://localhost:8000/api/sentiment?symbol=AAPL