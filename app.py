
import streamlit as st
import pandas as pd
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.prediction import predict_profile
from src.recommendations import (
    get_skill_gaps,
    get_roadmap,
    get_career_skill_tree,
)

st.set_page_config(
    page_title="CareerCompass",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- DESIGN THEME --------------------

st.markdown("""
<style>
:root {
    --navy: #243B63;
    --purple: #6558D3;
    --blue: #3478C8;
    --teal: #159A91;
    --coral: #E78365;
    --gold: #D6A23C;
    --ink: #20304A;
    --muted: #64748B;
    --canvas: #F2F5FB;
}

.stApp {
    background:
        radial-gradient(circle at 8% 5%, rgba(101,88,211,.10), transparent 26%),
        radial-gradient(circle at 95% 15%, rgba(21,154,145,.09), transparent 24%),
        var(--canvas);
    color: var(--ink);
    font-family: "Segoe UI", sans-serif;
}

.block-container {
    max-width: 1320px;
    padding-top: 1.8rem;
    padding-bottom: 3rem;
}

h1, h2, h3, h4 {
    color: var(--ink) !important;
    font-weight: 750 !important;
}

p, li, label {
    color: #43536B;
}

[data-testid="stSidebar"] {
    background: linear-gradient(
        165deg,
        #243B63 0%,
        #343D76 52%,
        #245D69 100%
    );
}

[data-testid="stSidebar"] * {
    color: #F5F7FF !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    background: rgba(255,255,255,.08);
    border-radius: 11px;
    padding: 9px 12px;
    margin: 4px 0;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: rgba(255,255,255,.18);
}

.hero {
    background: linear-gradient(
        115deg,
        #394F9B 0%,
        #6558D3 48%,
        #168F91 100%
    );
    padding: 34px 38px;
    border-radius: 22px;
    margin-bottom: 25px;
    box-shadow: 0 14px 34px rgba(54,69,137,.18);
}

.hero h1 {
    color: white !important;
    font-size: 34px !important;
    margin-bottom: 8px;
}

.hero p {
    color: #F1F5FF !important;
    font-size: 15px;
    line-height: 1.65;
}

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #E2E8F2;
    border-radius: 16px;
    padding: 17px 19px;
    box-shadow: 0 5px 18px rgba(36,54,86,.055);
}

[data-testid="stMetricLabel"] {
    color: #64748B !important;
}

[data-testid="stMetricValue"] {
    color: #394F9B !important;
    font-weight: 800;
}

.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(110deg, #6558D3, #3478C8);
    color: white !important;
    border: 0;
    border-radius: 10px;
    font-weight: 650;
    padding: .55rem 1.1rem;
}

.stButton > button:hover {
    filter: brightness(.94);
}

.cc-card {
    background: white;
    border: 1px solid #E1E7F0;
    border-radius: 16px;
    padding: 19px 20px;
    box-shadow: 0 5px 16px rgba(37,55,89,.045);
    min-height: 125px;
    margin-bottom: 12px;
}

.cc-card h3 {
    margin: 0 0 8px 0;
    font-size: 18px;
}

.cc-card p {
    margin: 0;
    color: #5D6B80;
    line-height: 1.55;
    font-size: 14px;
}

.pill {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 700;
    background: #EEEAFE;
    color: #5749B7;
    margin-bottom: 9px;
}

.roadmap-root {
    background: linear-gradient(
        120deg,
        #344C91,
        #6558D3 55%,
        #168F91
    );
    border-radius: 18px;
    padding: 22px;
    text-align: center;
    color: white;
    margin: 8px 0 16px;
}

.roadmap-root h2 {
    color: white !important;
    margin: 0;
    font-size: 24px;
}

.roadmap-root p {
    color: #E8ECFF !important;
    margin: 5px 0 0;
}

.skill-head {
    border-radius: 12px;
    padding: 13px 15px;
    margin: 8px 0;
    background: #F0F3FF;
    border-left: 5px solid #6558D3;
}

.topic-row {
    padding: 8px 11px;
    margin: 5px 0;
    background: #F7F9FC;
    border: 1px solid #E8EDF5;
    border-radius: 8px;
    color: #34445D;
}

[data-testid="stExpander"] {
    border: 1px solid #DDE5F0;
    border-radius: 12px;
    background: white;
}

hr {
    border-color: #DDE5F0;
}

@media(max-width: 768px) {
    .hero {
        padding: 24px 22px;
    }

    .hero h1 {
        font-size: 26px !important;
    }
}
</style>
""", unsafe_allow_html=True)


# -------------------- SESSION STATE --------------------

if "profile" not in st.session_state:
    st.session_state.profile = None

if "ranked" not in st.session_state:
    st.session_state.ranked = None


# -------------------- COMMON FUNCTIONS --------------------

def show_hero(title, subtitle):
    st.markdown(
        f"""
        <div class="hero">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def require_prediction():
    if (
        st.session_state.ranked is None
        or st.session_state.profile is None
    ):
        st.warning(
            "Please complete the Student Assessment "
            "and predict your career first."
        )
        return False

    return True


# -------------------- SIDEBAR --------------------

with st.sidebar:
    st.markdown("## 🧭 CareerCompass")
    st.caption("Intelligent Career Path Predictor")
    st.markdown("---")

    page = st.radio(
        "NAVIGATION",
        [
            "Home",
            "Student Assessment",
            "Career Prediction",
            "Skill Gap Analysis",
            "Learning Roadmap",
        ]
    )

    st.markdown("---")
    st.caption("MACHINE LEARNING • CAREER INTELLIGENCE")


# ====================================================
# HOME PAGE
# ====================================================

if page == "Home":

    show_hero(
        "Find your direction. Build your future.",
        "Discover suitable career paths, identify skill gaps "
        "and follow a structured learning roadmap."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Career pathways", "8")
    col2.metric("ML algorithms", "3")
    col3.metric("Learning roadmap", "Interactive")

    st.markdown("### How CareerCompass works")

    cols = st.columns(3)

    cards = [
        (
            "01 · Assess",
            "🧭",
            "Share your education, technical skills, strengths and interests."
        ),
        (
            "02 · Discover",
            "✨",
            "Explore your top career recommendations."
        ),
        (
            "03 · Grow",
            "🌱",
            "Understand skill gaps and follow a detailed learning path."
        ),
    ]

    for col, (heading, emoji, description) in zip(cols, cards):
        with col:
            st.markdown(
                f"""
                <div class="cc-card">
                    <span class="pill">{emoji} CAREER JOURNEY</span>
                    <h3>{heading}</h3>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("### Available career paths")

    st.write(
        "Data Analyst · Data Scientist · Machine Learning Engineer · "
        "Software Developer · Cybersecurity Analyst · Cloud Engineer · "
        "Business Analyst · UI/UX Designer"
    )

    st.info(
        "Note: This prototype uses synthetic training data. "
        "Model scores are not calibrated probabilities of career success. "
        "Learning roadmaps are illustrative guidance."
    )


# ====================================================
# STUDENT ASSESSMENT PAGE
# ====================================================

elif page == "Student Assessment":

    show_hero(
        "Student Assessment",
        "Tell us about your current skills, strengths and interests."
    )

    st.info("Rate each skill from 1 (Beginner) to 5 (Advanced).")

    with st.form("assessment_form"):

        left, right = st.columns(2)

        with left:

            st.subheader("🎓 Education")

            education = st.selectbox(
                "Highest qualification",
                [
                    "Diploma",
                    "Bachelor's degree",
                    "Master's degree"
                ]
            )

            education_map = {
                "Diploma": 1,
                "Bachelor's degree": 2,
                "Master's degree": 3
            }

            cgpa = st.slider(
                "CGPA / Academic Score",
                4.0, 10.0, 8.0, 0.1
            )

            st.subheader("💻 Technical Skills")

            python_skill = st.slider("Python", 1, 5, 3)
            java = st.slider("Java", 1, 5, 2)
            sql = st.slider("SQL", 1, 5, 3)
            statistics = st.slider("Statistics", 1, 5, 3)
            ml = st.slider("Machine Learning", 1, 5, 2)
            data_viz = st.slider("Data Visualization", 1, 5, 3)
            web = st.slider("Web Development", 1, 5, 2)
            cybersecurity = st.slider("Cybersecurity", 1, 5, 1)
            cloud = st.slider("Cloud Computing", 1, 5, 2)

        with right:

            st.subheader("💡 Strengths")

            design = st.slider("Design Skills", 1, 5, 2)
            communication = st.slider("Communication", 1, 5, 3)
            analytical = st.slider("Analytical Thinking", 1, 5, 3)
            creativity = st.slider("Creativity", 1, 5, 3)
            problem = st.slider("Problem Solving", 1, 5, 3)

            st.subheader("🎯 Interests")

            research_interest = st.slider("Research Interest", 1, 5, 3)
            business_interest = st.slider("Business Interest", 1, 5, 3)
            design_interest = st.slider("Design Interest", 1, 5, 2)
            security_interest = st.slider("Cybersecurity Interest", 1, 5, 2)
            infrastructure_interest = st.slider(
                "Cloud / Infrastructure Interest", 1, 5, 2
            )

        submitted = st.form_submit_button(
            "✨ Save Profile & Predict Careers",
            use_container_width=True
        )

    if submitted:

        profile = {
            "education_level": education_map[education],
            "cgpa": cgpa,
            "python": python_skill,
            "java": java,
            "sql": sql,
            "statistics": statistics,
            "machine_learning": ml,
            "data_visualization": data_viz,
            "web_development": web,
            "cybersecurity": cybersecurity,
            "cloud": cloud,
            "design": design,
            "communication": communication,
            "analytical_thinking": analytical,
            "creativity": creativity,
            "problem_solving": problem,
            "research_interest": research_interest,
            "business_interest": business_interest,
            "design_interest": design_interest,
            "security_interest": security_interest,
            "infrastructure_interest": infrastructure_interest,
        }

        try:
            ranked = predict_profile(profile)

            st.session_state.profile = profile
            st.session_state.ranked = ranked

            st.success(
                "Assessment completed! Open Career Prediction "
                "to view your recommendations."
            )

        except Exception as exc:
            st.error(f"Prediction error: {exc}")


# ====================================================
# CAREER PREDICTION PAGE
# ====================================================

elif page == "Career Prediction":

    show_hero(
        "Your Career Recommendations",
        "Explore career categories that match your submitted profile."
    )

    if require_prediction():

        ranked = st.session_state.ranked

        cols = st.columns(3)

        for i, (col, item) in enumerate(
            zip(cols, ranked[:3])
        ):

            with col:

                st.markdown(
                    f"""
                    <div class="cc-card">
                        <span class="pill">
                            RECOMMENDATION #{i + 1}
                        </span>
                        <h3>{item["career"]}</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.metric(
                    "Model score",
                    f'{item["score"] * 100:.1f}%'
                )

                st.progress(
                    min(1.0, max(0.0, float(item["score"])))
                )

        st.markdown("### All career categories")

        chart_df = pd.DataFrame(ranked).set_index("career")

        st.bar_chart(chart_df["score"])

        st.caption(
            "Model scores are outputs from a synthetic-data "
            "demonstration, not probabilities of career success."
        )


# ====================================================
# SKILL GAP ANALYSIS PAGE
# ====================================================

elif page == "Skill Gap Analysis":

    show_hero(
        "Skill Gap Analysis",
        "Compare your current skills with the target skills "
        "for your selected career."
    )

    if require_prediction():

        careers = [
            item["career"]
            for item in st.session_state.ranked
        ]

        chosen = st.selectbox(
            "Choose a career",
            careers
        )

        gaps = get_skill_gaps(
            chosen,
            st.session_state.profile
        )

        df = pd.DataFrame(gaps)

        st.markdown(f"### Skill profile: {chosen}")

        display_df = df.rename(
            columns={
                "skill": "Skill",
                "current": "Your Level",
                "required": "Target Level",
                "gap": "Gap"
            }
        )

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )

        chart = df.set_index("skill")[
            ["current", "required"]
        ]

        chart.columns = ["Your Level", "Target Level"]

        st.markdown("### Current level vs target level")

        st.bar_chart(chart)

        priorities = [
            item for item in gaps
            if item["gap"] > 0
        ]

        st.markdown("### Priority areas")

        if priorities:

            for item in priorities:

                st.write(
                    f"**{item['skill']}** — "
                    f"improve by approximately "
                    f"{item['gap']} level(s)."
                )

        else:

            st.success(
                "Your self-ratings meet the listed target levels."
            )

        st.caption(
            "Target levels are illustrative prototype requirements."
        )


# ====================================================
# LEARNING ROADMAP PAGE
# ====================================================

elif page == "Learning Roadmap":

    show_hero(
        "Your Career Skill Tree",
        "Explore the skills, detailed syllabus, exercises "
        "and mini-projects required for your selected career."
    )

    if require_prediction():

        careers = [
            item["career"]
            for item in st.session_state.ranked
        ]

        chosen = st.selectbox(
            "Choose your career roadmap",
            careers
        )

        gaps = get_skill_gaps(
            chosen,
            st.session_state.profile
        )

        tree = get_career_skill_tree(chosen)

        total_topics = sum(
            len(level["topics"])
            for skill in tree
            for level in skill["levels"]
        )

        priority_count = sum(
            1 for item in gaps
            if item["gap"] > 0
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Skill branches",
            len(tree)
        )

        col2.metric(
            "Skills to improve",
            priority_count
        )

        col3.metric(
            "Topics to learn",
            total_topics
        )

        # ROOT NODE

        st.markdown(
            f"""
            <div class="roadmap-root">
                <h2>🎯 {chosen}</h2>
                <p>
                    Career Goal → Core Skills → Learning Topics
                    → Practice → Portfolio Project
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### 🌿 Explore your skill branches")

        st.write(
            "Expand each skill to see its complete learning syllabus."
        )

        gap_lookup = {
            item["skill"]: item
            for item in gaps
        }

        for index, skill in enumerate(tree, start=1):

            gap_item = gap_lookup.get(
                skill["name"],
                {}
            )

            current = gap_item.get("current", 1)
            required = gap_item.get("required", 4)
            gap = gap_item.get("gap", 0)

            if gap > 0:
                icon = "🟠"
                priority = "Priority Skill"
            else:
                icon = "🟢"
                priority = "Target Met"

            with st.expander(
                f"{icon} {index}. {skill['name']} "
                f" | Current {current}/5 "
                f" → Target {required}/5 "
                f" | {priority}",
                expanded=(index == 1)
            ):

                st.markdown(
                    f"""
                    <div class="skill-head">
                        <strong>{skill["name"]}</strong><br>
                        <span>{skill["purpose"]}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if gap > 0:

                    st.warning(
                        f"Suggested improvement: "
                        f"{gap} skill level(s)."
                    )

                else:

                    st.success(
                        "Your self-rating meets this target."
                    )

                for level in skill["levels"]:

                    st.markdown(
                        f"#### {level['name']}"
                    )

                    st.caption(level["goal"])

                    st.markdown("**Topics to cover:**")

                    for topic in level["topics"]:

                        st.markdown(
                            f"""
                            <div class="topic-row">
                                📘 {topic}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    st.markdown(
                        "**Practice task:** "
                        + level["practice"]
                    )

                    if level.get("mini_project"):

                        st.markdown(
                            "**Mini-project:** "
                            + level["mini_project"]
                        )

                    st.divider()

        # CAPSTONE

        st.markdown("### 🏆 Final Capstone Project")

        st.markdown(
            f"""
            <div class="cc-card">
                <span class="pill">FINAL APPLICATION</span>
                <h3>{tree[0]["capstone_title"]}</h3>
                <p>{tree[0]["capstone"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # LEARNING ORDER

        st.markdown("### 📌 Recommended learning order")

        for step, skill in enumerate(tree, start=1):

            item = gap_lookup.get(skill["name"], {})

            label = (
                "Focus first"
                if item.get("gap", 0) > 0
                else "Maintain and practise"
            )

            st.write(
                f"**{step}. {skill['name']}** — {label}"
            )

        st.caption(
            "The ML model predicts career categories. "
            "The roadmap is a separate rule-based learning guide "
            "connected to your selected career and skill gaps."
        )
