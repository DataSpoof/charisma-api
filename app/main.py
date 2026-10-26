# uvicorn app.main:app --reload

# it is used for 👉 Faster event loop
# uvicorn app.main:app --workers 4 --loop uvloop --http httptools

from fastapi import FastAPI
from app.schema import InputData, PredictionResponse
from app.model_loader import model
from app.utils import preprocess
import numpy as np

app = FastAPI(title="Malware Detection API")

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

@app.post("/predict", response_model=PredictionResponse)
def predict(data: InputData):
    
    processed = preprocess(data.features)
    
    pred = model.predict(processed)[0][0]
    
    label = "malware" if pred > 0.5 else "benign"
    
    return {
        "prediction": label,
        "confidence": float(pred)
    }