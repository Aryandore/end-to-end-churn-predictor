from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

# 1. Initialize the App
app = FastAPI(title="Churn Prediction API")

# 2. Load the Model (We do this ONCE when the app starts)
try:
    model = joblib.load("models/churn_model.pkl")
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

# 3. Define the Input Format
# This ensures the user sends the correct data types.
class CustomerData(BaseModel):
    SeniorCitizen: int
    tenure: int
    MonthlyCharges: float
    # Add other numerical columns if your model used them!

# 4. Define the Prediction Endpoint
@app.post("/predict")
def predict_churn(customer: CustomerData):
    if not model:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    # Convert input data to DataFrame (what the model expects)
    input_df = pd.DataFrame([customer.dict()])
    
    # Make prediction
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[0][1] # Probability of Churn (1)
    
    # Return JSON result
    return {
        "churn_prediction": int(prediction[0]),
        "churn_probability": float(probability),
        "message": "High Risk" if prediction[0] == 1 else "Safe"
    }

# 5. Root Endpoint (Just to check if it's running)
@app.get("/")
def read_root():
    return {"message": "Churn API is running!"}