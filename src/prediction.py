from pathlib import Path
import json
import joblib
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "career_model.joblib"
META_PATH = ROOT / "models" / "model_metadata.json"

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Model not found. Run: python -m src.train_model")
    return joblib.load(MODEL_PATH)

def load_metadata():
    if META_PATH.exists():
        return json.loads(META_PATH.read_text())
    return {}

def predict_profile(profile):
    model = load_model()
    X = pd.DataFrame([profile])
    probabilities = model.predict_proba(X)[0]
    classes = model.classes_
    ranked = sorted(
        [{"career": str(c), "score": float(p)} for c, p in zip(classes, probabilities)],
        key=lambda item: item["score"], reverse=True
    )
    return ranked
