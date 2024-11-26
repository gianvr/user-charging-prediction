import pickle

import pandas as pd
from fastapi import FastAPI

from schemas import PredictionInput, PredictionOutput

app = FastAPI()


with open("./models/model.pkl", "rb") as f:
    model = pickle.load(f)


@app.post(
    "/predict",
    response_model=PredictionOutput,
    responses={
        200: {
            "description": "Prediction output",
            "content": {
                "application/json": {
                    "example": {"prediction": "Long-Distance Traveler"}
                }
            },
        },
    },
)
async def predict(input_data: PredictionInput):
    data = pd.DataFrame([input_data.model_dump()])

    new_name_columns = {
        "Vehicle_Model": "Vehicle Model",
        "Charging_Station_Location": "Charging Station Location",
        "Time_of_Day": "Time of Day",
        "Day_of_Week": "Day of Week",
        "Charger_Type": "Charger Type",
        "Battery_Capacity": "Battery Capacity (kWh)",
        "Charging_Cost": "Charging Cost (USD)",
        "Charging_Duration": "Charging Duration (hours)",
        "Charging_Rate": "Charging Rate (kW)",
        "Distance_Driven": "Distance Driven (since last charge) (km)",
        "Energy_Consumed": "Energy Consumed (kWh)",
        "State_of_Charge_End": "State of Charge (End %)",
        "State_of_Charge_Start": "State of Charge (Start %)",
        "Temperature": "Temperature (°C)",
        "Vehicle_Age": "Vehicle Age (years)",
    }

    data = data.rename(columns=new_name_columns)

    prediction = model.predict(data)

    return PredictionOutput(prediction=prediction[0])
