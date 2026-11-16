from pathlib import Path
import json
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "dataset" / "career_dataset.csv"
MODEL_DIR = ROOT / "models"
MODEL_DIR.mkdir(exist_ok=True)

def train():
    data = pd.read_csv(DATA_PATH)
    X = data.drop(columns=["career"])
    y = data["career"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    candidates = {
        "Logistic Regression": Pipeline([
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(max_iter=2000, class_weight="balanced"))
        ]),
        "Decision Tree": DecisionTreeClassifier(
            max_depth=12, min_samples_leaf=3, random_state=42, class_weight="balanced"
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=300, max_depth=14, min_samples_leaf=2,
            random_state=42, class_weight="balanced"
        )
    }
    results = {}
    best_name, best_model, best_score = None, None, -1
    for name, model in candidates.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        score = f1_score(y_test, pred, average="macro")
        cv = cross_val_score(model, X_train, y_train, cv=5, scoring="f1_macro").mean()
        results[name] = {
            "test_accuracy": round(float(accuracy_score(y_test, pred)), 4),
            "test_macro_f1": round(float(score), 4),
            "cv_macro_f1": round(float(cv), 4)
        }
        if score > best_score:
            best_name, best_model, best_score = name, model, score

    joblib.dump(best_model, MODEL_DIR / "career_model.joblib")
    metadata = {
        "best_model": best_name,
        "results": results,
        "features": list(X.columns),
        "classes": sorted(y.unique().tolist()),
        "dataset_rows": int(len(data)),
        "data_note": "Synthetic demonstration dataset; not validated for real career guidance."
    }
    (MODEL_DIR / "model_metadata.json").write_text(json.dumps(metadata, indent=2))
    report = classification_report(y_test, best_model.predict(X_test), output_dict=True)
    (MODEL_DIR / "classification_report.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(metadata, indent=2))
    return metadata

if __name__ == "__main__":
    train()
