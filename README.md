# CareerCompass – ML-Based Career Recommendation System

CareerCompass is a Machine Learning-based career recommendation and skill-gap analysis application that helps students identify suitable career paths based on their academic background, technical skills, soft skills, and personal interests.

The application uses classification algorithms to recommend suitable career options and provides personalized skill-gap analysis, learning roadmaps, and career-specific skill trees to help students understand what they need to learn to achieve their career goals.

## Project Overview

Choosing the right career can be challenging for students, especially when they are unsure about their strengths, interests, and required industry skills.

CareerCompass addresses this problem by analyzing student profiles and recommending suitable career paths using Machine Learning.

The application also helps students understand their skill gaps and provides structured learning guidance to improve their skills.

## Key Features

- **Student Profile Assessment:** Collects academic details, technical skills, soft skills, and career interests.
- **ML-Based Career Prediction:** Recommends suitable careers using a trained classification model.
- **Career Ranking:** Displays ranked career recommendations with prediction scores.
- **Skill-Gap Analysis:** Compares existing student skills with the required skills for a selected career.
- **Personalized Learning Roadmap:** Provides a three-stage learning roadmap.
- **Interactive Skill Tree:** Displays career-specific skills, topics, practice activities, and projects.
- **Career Exploration:** Supports eight different career categories.
- **Interactive Dashboard:** Provides a user-friendly Streamlit interface.

## Career Categories

The model predicts one of the following eight career categories:

1. Data Analyst
2. Data Scientist
3. Machine Learning Engineer
4. Software Developer
5. Cybersecurity Analyst
6. Cloud Engineer
7. Business Analyst
8. UI/UX Designer

## Input Features

The model uses 21 input features to understand a student's profile.

| Category | Features |
|---|---|
| Academic | Education Level, CGPA |
| Technical Skills | Python, Java, SQL, Statistics, Machine Learning, Data Visualization, Web Development, Cybersecurity, Cloud, Design |
| Soft Skills | Communication, Analytical Thinking, Creativity, Problem Solving |
| Career Interests | Research Interest, Business Interest, Design Interest, Security Interest, Infrastructure Interest |

## Machine Learning Methodology

### Dataset

- Total records: 1,440
- Input features: 21
- Target variable: Career
- Career categories: 8
- Dataset type: Synthetic demonstration dataset

### Algorithms Implemented

Three classification algorithms were trained and evaluated:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

### Model Training Process

- Train-test split: 80:20
- Random state: 42
- Stratified sampling
- 5-fold cross-validation
- Class balancing using `class_weight="balanced"`
- StandardScaler applied within the Logistic Regression pipeline

### Model Evaluation

The models were evaluated using:

- Accuracy
- Macro F1-score
- Cross-validation Macro F1-score

| Algorithm | Test Accuracy | Test Macro F1 | CV Macro F1 |
|---|---:|---:|---:|
| Logistic Regression | 94.79% | 94.79% | 94.89% |
| Decision Tree | 80.56% | 80.72% | 79.33% |
| Random Forest | 93.40% | 93.39% | 92.39% |

### Best Performing Model

Logistic Regression achieved the highest test Macro F1-score of **94.79%** and was selected as the final classification model.

The trained model is saved and reused by the application for career predictions.

## Application Workflow

1. Student opens the CareerCompass application.
2. Completes the career assessment form.
3. Enters academic details, technical skills, soft skills, and interests.
4. The trained ML model analyzes the student profile.
5. The application displays ranked career recommendations.
6. Student selects a career to explore.
7. The application performs skill-gap analysis.
8. A structured learning roadmap and career-specific skill tree are displayed.

## Skill-Gap Analysis

CareerCompass compares the student's current skill level with the required skill level for a selected career.

The skill gap is calculated using:

`Skill Gap = max(0, Required Skill Level - Current Skill Level)`

The application identifies skills that need improvement and helps students prioritize their learning.

## Learning Roadmap

The learning roadmap is organized into three stages:

### Level 1 – Foundations
- Understand basic concepts.
- Learn fundamental tools and technologies.
- Practice essential skills.

### Level 2 – Intermediate
- Apply concepts to practical problems.
- Work on mini-projects.
- Improve technical proficiency.

### Level 3 – Advanced Application
- Learn advanced concepts.
- Build practical applications.
- Complete career-oriented capstone projects.

## Career Skill Tree

The application provides a structured skill tree for each career.

Each skill contains:
- Skill purpose
- Foundation-level topics
- Intermediate-level topics
- Advanced-level topics
- Practice activities
- Mini-projects
- Capstone projects

This helps students follow a structured learning path instead of learning random topics.

## Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Data Visualization
- Plotly

### Application Framework
- Streamlit

### Development Tools
- Visual Studio Code
- Git
- GitHub

## Project Structure

```text
CareerCompass/
│
├── app.py
│
├── dataset/
│   └── career_dataset.csv
│
├── models/
│   ├── career_model.pkl
│   ├── model_metadata.json
│   └── classification_report.json
│
├── src/
│   ├── __init__.py
│   ├── train_model.py
│   ├── prediction.py
│   └── recommendations.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: The folder structure above represents the expected organization. Adjust filenames if your actual Streamlit project uses different names.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/CareerCompass.git
```

### 2. Navigate to the Project Folder

```bash
cd CareerCompass
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows PowerShell:

```powershell
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## Model Training

To train the classification model again, execute:

```bash
python -m src.train_model
```

The training process evaluates the three classification algorithms and saves the selected model and evaluation reports in the models directory.

If the trained model files are already included in the repository, retraining is not required to run the application.

## Model Artifacts

The project generates the following model-related files:

| File | Description |
|---|---|
| `career_model.pkl` | Saved trained classification model (if this is the actual filename in your Streamlit project) |
| `model_metadata.json` | Model comparison results and metadata |
| `classification_report.json` | Classification evaluation report |

## Future Enhancements

- Integrate real-world student datasets.
- Improve career recommendations using additional ML techniques.
- Add user authentication and profile management.
- Include industry-specific job role recommendations.
- Integrate external learning resources and course recommendations.
- Add career demand and salary insights.
- Deploy the application for wider accessibility.

## Limitations

- The current dataset is synthetic and intended for demonstration purposes.
- The model has not been validated using representative real-world student data.
- Career recommendations should be treated as guidance rather than definitive career decisions.
- Skill requirements are predefined within the recommendation logic and may not represent every employer's expectations.

## Conclusion

CareerCompass combines Machine Learning-based classification with skill-gap analysis and structured learning roadmaps to help students explore potential career paths.

It demonstrates how Machine Learning can be integrated into an interactive application to support career exploration and personalized learning guidance.

**Developed using Python, Machine Learning, Scikit-learn, and Streamlit.**
