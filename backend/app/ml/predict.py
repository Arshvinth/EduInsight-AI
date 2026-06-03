import joblib
from pathlib import Path
import numpy as np
from fastapi import HTTPException


# Resolve model path relative to the repository so cwd doesn't matter
BASE_DIR = Path(__file__).resolve().parents[2]  # backend/
MODEL_PATH = BASE_DIR / "app" / "ml" / "model.pkl"

# Lazy-loaded model to avoid import-time crashes when file is missing
_model = None


def _load_model():
    global _model
    if _model is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(f"Trained model not found at {MODEL_PATH}. Run the training script: python app/ml/train_risk_model.py")
        _model = joblib.load(MODEL_PATH)
    return _model


def predict_risk(attendance: float, cgpa: float, failed_modules: int, recent_marks: float):
    try:
        model = _load_model()
    except FileNotFoundError as e:
        # Return a clear HTTP error for the API route
        raise HTTPException(status_code=500, detail=str(e))

    features = np.array([[attendance, cgpa, failed_modules, recent_marks]])
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return {
        "prediction": "at_risk" if prediction == 1 else "safe",
        "risk_score": round(float(probability), 2)
    }