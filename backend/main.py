import os
from fastapi import FastAPI
from backend.service.analysis import analyze_investment
import uvicorn

app = FastAPI()

@app.get("/analyze/{symbol}")
def analyze(symbol: str):
    result = analyze_investment(symbol)
    return result

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )
