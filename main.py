import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="HIV Risk Prediction API")

model = joblib.load("hiv_risk_model.pkl")

class PatientData(BaseModel):
    age: float
    Gender: str
    key_population_type: str
    sti_results: str
    tb_results: str
    HTSEntryPoint: str

@app.post("/predict")
def predict(data: PatientData):
    input_df = pd.DataFrame([data.dict()])
    risk_proba = float(model.predict_proba(input_df)[0, 1])
    return {"risk_probability": risk_proba, "risk_status": "High Risk" if risk_proba >= 0.2 else "Low Risk"}
