import yfinance as yf

#Define the ticker symbol
tickerSymbol = 'AAPL'

#Create a ticker object
ticker = yf.Ticker(tickerSymbol)

#Fetch historical market data
historica_data = ticker.history(period='1y')
print(f"Historical Data for {tickerSymbol}:")
print(historica_data)

#Fetch basic financials
financials = ticker.financials
print(f"\nFinancials for {tickerSymbol}:")
print(financials)

#Fetch stock actions like dividends and splits
actions = ticker.actions
print("\nStock Actions:")
print(actions)
