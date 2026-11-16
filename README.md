# CareerCompass – Intelligent Career Path Predictor

A presentation-ready Machine Learning prototype built with Python, scikit-learn and Streamlit.

## Features
- Student profile assessment (education, technical skills, strengths and interests)
- Multiclass career-category prediction
- Top-three career ranking
- Skill-gap comparison
- Rule-based learning roadmap
- Model comparison: Logistic Regression, Decision Tree and Random Forest

## Important data limitation
The included `dataset/career_dataset.csv` is a **synthetic demonstration dataset** generated from illustrative skill profiles. It is useful for demonstrating the ML workflow, but it is not real student outcome data and has not been validated for career guidance. The displayed model scores are not probabilities of career success. Skill requirements and roadmap suggestions are illustrative.

For a real-world version, replace this dataset with properly sourced occupational skill data and ethically collected, consented profile/label data. Validate recommendations with career experts and users before deployment.

## Run in VS Code

### 1. Extract the ZIP and open the CareerCompass folder

### 2. Create and activate a virtual environment

Windows PowerShell:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the model (optional; a trained model is included)
```bash
python -m src.train_model
```

This compares three classifiers and saves the best model by held-out macro F1 score to `models/career_model.joblib`.

### 5. Start Streamlit
```bash
streamlit run app.py
```

The app opens in your browser, usually at `http://localhost:8501`.

## Project structure
```text
CareerCompass/
├── app.py
├── dataset/
│   └── career_dataset.csv
├── models/
│   ├── career_model.joblib
│   ├── model_metadata.json
│   └── classification_report.json
├── src/
│   ├── train_model.py
│   ├── prediction.py
│   └── recommendations.py
├── presentation/
│   └── project_documentation.md
└── requirements.txt
```

## ML workflow
1. Load structured profile dataset.
2. Split into training and test sets using stratification.
3. Train Logistic Regression, Decision Tree and Random Forest.
4. Compare held-out macro F1 and cross-validation macro F1.
5. Save the best-performing model.
6. Use the same feature schema to score a new profile.

## Inputs
Education level, CGPA, self-rated technical skills, strengths and interest ratings.

## Outputs
Ranked career categories, model scores, skill-gap table and learning steps.

## Presentation note
Explain clearly that the included data is synthetic and that the project is a prototype. Do not claim the prototype can determine a person's true career, guarantee employment, or predict career success.
