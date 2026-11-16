# CareerCompass – Project Presentation Notes

## Problem statement
Students and early-career learners may find it difficult to connect their current skills, interests and educational background with possible career directions. CareerCompass demonstrates a data-driven way to explore career categories and identify skills to strengthen.

## Aim
Build a supervised multiclass classification prototype that ranks eight career categories from a structured profile, then presents a skill-gap comparison and learning suggestions.

## Input features
- Education level and CGPA
- Python, Java, SQL, statistics, machine learning, data visualization
- Web development, cybersecurity, cloud and design
- Communication, analytical thinking, creativity and problem solving
- Research, business, design, security and infrastructure interests

## Output
- Ranked top-three career categories
- Model output scores for all eight classes
- Skill comparison for a selected career
- Illustrative learning roadmap

## Algorithms compared
- Logistic Regression (scaled numeric features)
- Decision Tree
- Random Forest

The selected model is based on held-out macro F1 score. The training script also reports five-fold cross-validation macro F1 on the training partition.

## Workflow
Data generation/loading → preprocessing/model pipeline → stratified train/test split → model comparison → evaluation → model serialization → Streamlit input → prediction → skill-gap and roadmap views.

## Limitations and ethical considerations
The included dataset is synthetic and its labels are generated from illustrative role profiles. Consequently, test scores only measure how well models learn patterns in this synthetic dataset. They do not establish real-world accuracy or fairness. Self-ratings can be subjective; educational and demographic proxies can introduce bias. The application must be treated as an exploration aid, not a hiring tool or authoritative career counselor.

## Future work
1. Replace synthetic examples with sourced occupational skill taxonomies and consented, validated profile data.
2. Evaluate with real users and career professionals.
3. Add explainability (e.g. SHAP) and calibrated confidence.
4. Add job-market trend data with source and date tracking.
5. Add resume parsing with NLP and portfolio analysis.
6. Add an LLM-based conversational career mentor grounded in verified sources.
7. Build a Flask API version that reuses the trained model.
