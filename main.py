from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(
    title="FitIntel AI API",
    version="1.0"
)

# Load trained models
goal_model = joblib.load("models/goal_achievement/goal_model.pkl")
calorie_model = joblib.load("models/calorie_prediction/calorie_model.pkl")


# -------------------------------
# Input model for Goal Prediction
# -------------------------------
class GoalInput(BaseModel):
    TotalDistance: float
    VeryActiveMinutes: int
    FairlyActiveMinutes: int
    LightlyActiveMinutes: int
    SedentaryMinutes: int
    Calories: int


# ---------------------------------
# Input model for Calorie Prediction
# ---------------------------------
class CalorieInput(BaseModel):
    TotalSteps: int
    TotalDistance: float
    VeryActiveMinutes: int
    FairlyActiveMinutes: int
    LightlyActiveMinutes: int
    SedentaryMinutes: int


@app.get("/")
def home():
    return {
        "message": "FitIntel AI API Running"
    }


@app.post("/predict_goal")
def predict_goal(data: GoalInput):

    prediction = goal_model.predict([[
        data.TotalDistance,
        data.VeryActiveMinutes,
        data.FairlyActiveMinutes,
        data.LightlyActiveMinutes,
        data.SedentaryMinutes,
        data.Calories
    ]])

    return {
        "Goal Achieved": bool(prediction[0])
    }


@app.post("/predict_calories")
def predict_calories(data: CalorieInput):

    prediction = calorie_model.predict([[
        data.TotalSteps,
        data.TotalDistance,
        data.VeryActiveMinutes,
        data.FairlyActiveMinutes,
        data.LightlyActiveMinutes,
        data.SedentaryMinutes
    ]])

    return {
        "Predicted Calories": round(float(prediction[0]), 2)
    }