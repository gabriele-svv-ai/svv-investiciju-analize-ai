from fastapi import FastAPI
from service.analysis import analyze_investment

app = FastAPI()

@app.get("/analyze/{symbol}")
def analyze(symbol: str):
    result = analyze_investment(symbol)
    return result

