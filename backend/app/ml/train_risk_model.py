import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# Resolve paths relative to this script so cwd doesn't matter
BASE_DIR = Path(__file__).resolve().parents[2]  # points to backend/
DATA_PATH = BASE_DIR / "data" / "student_risk_dataset.csv"
MODEL_PATH = Path(__file__).resolve().parent / "model.pkl"

# Load dataset from CSV
data = pd.read_csv(DATA_PATH)

# Features used for prediction
X = data[["attendance", "cgpa", "failed_modules", "recent_marks"]]

# Target label
y = data["risk_label"]

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create a simple classifier
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(model, MODEL_PATH)

print(f"Model saved to {MODEL_PATH}")