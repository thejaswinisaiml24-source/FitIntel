import streamlit as st
import streamlit.components.v1 as components
# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="FitIntel AI",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# LOAD CSS
# ============================================================

def load_css():
    try:
        with open(
            "dashboard/assets/style.css",
            "r",
            encoding="utf-8"
        ) as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        st.error("❌ CSS file not found.")


load_css()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("# 💪 FitIntel AI")

    st.caption(
        "AI-Powered Fitness Analytics Platform"
    )

    st.divider()

    st.success("🟢 AI Engine Online")

    st.markdown("### 🧩 Technologies")

    st.markdown(
        """
        🐍 **Python**

        📊 **Streamlit**

        ⚡ **FastAPI**

        🤖 **Scikit-Learn**

        🗄️ **SQLite**

        📈 **Plotly**
        """
    )

    st.divider()

    st.markdown("### 📌 Platform")

    st.markdown(
        """
        **Analytics**

        **Predictions**

        **AI Coach**

        **Reports**
        """
    )

    st.divider()

    st.info("FitIntel AI • v1.0")


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">💪 FitIntel AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">AI-Powered Fitness Analytics & Prediction Platform</div>',
    unsafe_allow_html=True
)


# ============================================================
# FITNESS HERO
# ============================================================

try:
    with open(
        "dashboard/assets/style.css",
        "r",
        encoding="utf-8"
    ) as f:
        hero_css = f.read()
except FileNotFoundError:
    hero_css = ""


hero_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<style>

{hero_css}

/* ----------------------------------------------------------
   HERO IFRAME FIX
   ---------------------------------------------------------- */

html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    background: transparent;
}}

body {{
    overflow: hidden;
}}

</style>

</head>

<body>

<div class="fi-fitness-hero">

    <div class="fi-sunlight"></div>

    <div class="fi-sun"></div>

    <div class="fi-cloud fi-cloud-1"></div>
    <div class="fi-cloud fi-cloud-2"></div>

    <div class="fi-tree fi-tree-1"></div>
    <div class="fi-tree fi-tree-2"></div>
    <div class="fi-tree fi-tree-3"></div>

    <div class="fi-jogger">

        <div class="fi-jogger-head"></div>

        <div class="fi-jogger-body"></div>

        <div class="fi-jogger-arm"></div>
        <div class="fi-jogger-arm right"></div>

        <div class="fi-jogger-leg"></div>
        <div class="fi-jogger-leg right"></div>

    </div>

    <div class="fi-track"></div>

    <div class="fi-hero-content">

        <div class="fi-hero-badge">
            ✦ DAILY FITNESS
        </div>

        <div class="fi-hero-title">
            Move Better. Live Better.
        </div>

        <div class="fi-hero-subtitle">
            Track your activity, understand your progress,
            and let FitIntel AI guide your fitness journey.
        </div>

    </div>

</div>

</body>
</html>
"""


components.html(
    hero_html,
    height=430,
    scrolling=False
)
# ============================================================
# WELCOME
# ============================================================

st.success(
    "✨ WELCOME TO FITINTEL AI"
)

st.markdown(
    "## Your fitness data. Your insights. Your progress."
)

st.write(
    """
    FitIntel AI analyzes Fitbit activity data, identifies fitness
    patterns, predicts outcomes using Machine Learning, and
    converts your data into actionable insights.
    """
)


# ============================================================
# PLATFORM OVERVIEW
# ============================================================

st.divider()

st.subheader("📊 Platform Overview")

st.caption(
    "Everything you need to understand and improve your fitness."
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("## 📊 Analytics")
    st.write(
        "Explore activity trends, steps, calories, distance, "
        "activity levels and fitness patterns."
    )

with c2:
    st.markdown("## 🔮 Predictions")
    st.write(
        "Use Machine Learning models to predict goal "
        "achievement and estimate calorie burn."
    )

with c3:
    st.markdown("## 🤖 AI Coach")
    st.write(
        "Get personalized activity insights and practical "
        "recommendations based on your fitness data."
    )


# ============================================================
# WORKFLOW
# ============================================================

st.divider()

st.subheader("⚙️ How FitIntel AI Works")

st.caption(
    "From raw fitness data to intelligent recommendations."
)

workflow = [
    ("📱", "Fitbit Data", "Activity records"),
    ("🧹", "Preprocessing", "Clean & transform"),
    ("🧠", "Machine Learning", "Learn patterns"),
    ("⚡", "FastAPI", "Serve predictions"),
    ("📊", "Dashboard", "Insights & actions"),
]

columns = st.columns(5)

for column, item in zip(columns, workflow):

    icon, title, description = item

    with column:
        st.markdown(f"## {icon}")
        st.markdown(f"**{title}**")
        st.caption(description)


# ============================================================
# PROJECT MODULES
# ============================================================

st.divider()

st.subheader("🧩 Project Modules")

st.caption(
    "Explore each part of the FitIntel AI platform from the sidebar."
)

m1, m2, m3 = st.columns(3)

with m1:

    st.markdown("## 📊 Analytics")

    st.write(
        "Understand your fitness data through interactive "
        "charts and statistical analysis."
    )

    st.markdown(
        """
        - Daily activity trends
        - Step distribution
        - Calories analysis
        - Correlation analysis
        """
    )


with m2:

    st.markdown("## 🔮 Prediction Center")

    st.write(
        "Use trained Machine Learning models to generate "
        "fitness predictions."
    )

    st.markdown(
        """
        - Goal achievement
        - Calorie prediction
        - Prediction confidence
        - Model-driven insights
        """
    )


with m3:

    st.markdown("## 🤖 AI Coach")

    st.write(
        "Convert fitness measurements into practical "
        "personalized recommendations."
    )

    st.markdown(
        """
        - Activity suggestions
        - Fitness insights
        - Goal guidance
        - Personalized recommendations
        """
    )


# ============================================================
# TECHNOLOGY STACK
# ============================================================

st.divider()

st.subheader("🛠️ Technology Stack")

t1, t2, t3 = st.columns(3)

with t1:

    st.info(
        """
        ### ⚡ Backend

        - Python
        - FastAPI
        - Uvicorn
        - SQLite
        """
    )

with t2:

    st.info(
        """
        ### 🤖 Machine Learning

        - Pandas
        - NumPy
        - Scikit-Learn
        - Random Forest
        - Joblib
        """
    )

with t3:

    st.info(
        """
        ### 📈 Visualization

        - Streamlit
        - Plotly
        - Interactive Charts
        - Data Analytics
        """
    )


# ============================================================
# PIPELINE
# ============================================================

st.divider()

st.subheader("🔄 FitIntel AI Pipeline")

st.info(
    """
    **DATA → INTELLIGENCE → ACTION**

    ### Transforming fitness data into decisions

    📱 Fitbit Dataset
    →
    🧹 Data Cleaning
    →
    ⚙️ Feature Engineering
    →
    🧠 ML Models
    →
    ⚡ FastAPI
    →
    📊 Streamlit
    →
    💡 Fitness Insights
    """
)


# ============================================================
# ABOUT
# ============================================================

st.divider()

st.subheader("ℹ️ About FitIntel AI")

st.markdown(
    """
    ### AI-Powered Fitness Analytics Platform

    FitIntel AI is an end-to-end fitness analytics platform
    developed using Python, Machine Learning, FastAPI,
    SQLite, Plotly and Streamlit.

    The system analyzes Fitbit activity data and transforms
    raw measurements such as steps, distance, calories and
    activity minutes into meaningful analytics and Machine
    Learning predictions.

    The platform demonstrates the complete data science lifecycle:

    **Data Collection → Data Cleaning → Feature Engineering
    → Machine Learning → Model Deployment
    → Interactive Visualization → Fitness Recommendations**
    """
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div style="
        text-align:center;
        padding:25px 0;
        color:#64748B;
        font-size:13px;
    ">
        <strong style="font-size:18px;color:#1E3A8A;">
            💪 FitIntel AI
        </strong>
        <br><br>
        Developed by <strong>Thejaswini S</strong>
        <br>
        B.E Computer Science & Engineering (AI & ML)
        <br>
        AI-Powered Fitness Analytics • Version 1.0
    </div>
    """,
    unsafe_allow_html=True
)