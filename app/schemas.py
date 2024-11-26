from typing import Literal

from pydantic import BaseModel, Field


class PredictionInput(BaseModel):
    Vehicle_Model: Literal["Hyundai Kona", "Nissan Leaf", "Chevy Bolt", "BMW i3", "Tesla Model 3"] = Field(..., example="Hyundai Kona")
    Charging_Station_Location: Literal["San Francisco", "Houston", "Los Angeles", "Chicago", "New York"] = Field(..., example="Houston")
    Time_of_Day: Literal["Morning", "Evening", "Afternoon", "Night"] = Field(..., example="Evening")
    Day_of_Week: Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] = Field(..., example="Saturday")
    Charger_Type: Literal["Level 1", "DC Fast Charger", "Level 2"] = Field(..., example="Level 1")
    Battery_Capacity: float = Field(..., example=50.0)
    Charging_Cost: float = Field(..., example=13.04)
    Charging_Duration: float = Field(..., example=1.27)
    Charging_Rate: float = Field(..., example=32.88)
    Distance_Driven: float = Field(..., example=199.58)
    Energy_Consumed: float = Field(..., example=79.46)
    State_of_Charge_End: float = Field(..., example=99.62)
    State_of_Charge_Start: float = Field(..., example=83.12)
    Temperature: float = Field(..., example=38.32)
    Vehicle_Age: float = Field(..., example=1.0)


class PredictionOutput(BaseModel):
    prediction: str