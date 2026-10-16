import os
from fastapi import FastAPI
from backend.service.analysis_svv import analyze_svv_project
import uvicorn
import traceback

app = FastAPI()

@app.post("/analyze_svv")
def analyze_svv(initial_investment: float, cash_flows: list[float], discount_rate: float):
    try:
        result = analyze_svv_project(
            initial_investment=initial_investment,
            yearly_cash_flows=cash_flows,
            discount_rate=discount_rate
        )
        return result
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )
