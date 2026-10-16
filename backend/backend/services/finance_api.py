import yfinance as yf

def get_stock_data(symbol):
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period="5y")
    return hist["Close"].tolist()
