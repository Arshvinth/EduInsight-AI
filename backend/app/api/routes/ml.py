from fastapi import APIRouter
from app.schemas.ml import RiskPredictionRequest, RiskPredictionResponse
from app.ml.predict import predict_risk


# Router for ML endpoints
router = APIRouter(prefix="/ml", tags=["ML"])


# Predict whether a student is at risk
@router.post("/predict-risk", response_model=RiskPredictionResponse)
def predict_student_risk(request: RiskPredictionRequest):
    result = predict_risk(
        attendance=request.attendance,
        cgpa=request.cgpa,
        failed_modules=request.failed_modules,
        recent_marks=request.recent_marks
    )
    return result