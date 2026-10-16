import os
from fastapi import FastAPI
from backend.service.analysis import analyze_investment
import uvicorn

app = FastAPI()

@app.get("/analyze/{symbol}")
def analyze(symbol: str):
    try:
        result = analyze_investment(symbol)
        return result
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )

