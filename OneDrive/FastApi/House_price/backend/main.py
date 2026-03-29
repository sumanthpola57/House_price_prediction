from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI()



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "model", "xgb.pkl")

model = joblib.load(model_path)

class HouseData(BaseModel):
    bedrooms: int
    bathrooms: float
    sqft_living: float
    sqft_lot: float
    floors: float
    waterfront: int
    view: int
    condition: int
    grade: int
    sqft_above: float
    sqft_basement: float
    yr_built: int
    yr_renovated: int
    zipcode: int
    lat: float
    long: float
    sqft_living15: float
    sqft_lot15: float


@app.get("/")
def home():
    return {"message": "working mawa"}



@app.post("/predict")
def predict(data: HouseData):
    features = np.array([[ 
    data.bedrooms,
    data.bathrooms,
    data.sqft_living,
    data.sqft_lot,
    data.floors,
    data.waterfront,
    data.view,
    data.condition,
    data.grade,
    data.sqft_above,
    data.sqft_basement,
    data.yr_built,
    data.yr_renovated,
    data.zipcode,
    data.lat,
    data.long,
    data.sqft_living15,
    data.sqft_lot15
]])
    raw_pred = model.predict(features)
    print("RAW:", raw_pred)

    prediction = np.expm1(raw_pred)
    return {"prediction": float(prediction[0])}