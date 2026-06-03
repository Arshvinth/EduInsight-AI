from pydantic import BaseModel


# Request body for risk prediction
class RiskPredictionRequest(BaseModel):
    attendance: float
    cgpa: float
    failed_modules: int
    recent_marks: float


# Response body for risk prediction
class RiskPredictionResponse(BaseModel):
    prediction: str
    risk_score: float