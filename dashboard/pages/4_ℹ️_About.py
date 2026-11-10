import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("💪 FitIntel AI")

st.markdown("""
### AI-Powered Fitness Analytics Platform

An intelligent fitness analytics platform that combines Machine Learning,
interactive dashboards and AI-powered recommendations to help users
understand and improve their daily fitness activities.
""")

st.divider()

# ---------------------------------------------------
# PROJECT OVERVIEW
# ---------------------------------------------------

st.subheader("📌 Project Overview")

st.write("""
FitIntel AI is a complete fitness analytics platform developed using
Python, FastAPI, Streamlit and Machine Learning.

The application analyzes Fitbit daily activity data to provide:

• Fitness Analytics

• Goal Achievement Prediction

• Calorie Burn Prediction

• AI-based Health Recommendations

• Interactive Dashboards

• Downloadable Reports

The system helps users monitor their physical activity,
identify health trends and make data-driven lifestyle decisions.
""")

st.divider()
# ---------------------------------------------------
# KEY FEATURES
# ---------------------------------------------------

st.subheader("⭐ Key Features")

col1, col2, col3 = st.columns(3)

with col1:

    st.info("""
### 🤖 Goal Prediction

Predict whether a user will achieve the recommended
10,000 daily step goal using Machine Learning.
""")

    st.success("""
### 🔥 Calorie Prediction

Estimate daily calorie burn using
a trained Random Forest Regression model.
""")

with col2:

    st.warning("""
### 📈 Analytics Dashboard

Interactive Plotly dashboards with
KPIs, trends, filters and health insights.
""")

    st.info("""
### 🧠 AI Coach

Provides personalized fitness recommendations,
wellness score and health analysis.
""")

with col3:

    st.success("""
### 📄 Reports

Generate AI-powered fitness reports
and export them as downloadable files.
""")

    st.warning("""
### 📊 Data Visualization

Visualize activity trends,
calorie distribution,
goal achievement and correlations.
""")

st.divider()

# ---------------------------------------------------
# PROJECT MODULES
# ---------------------------------------------------

st.subheader("📂 Project Modules")

modules = {
    "🏠 Dashboard":
        "Overview of fitness KPIs and quick insights.",

    "📈 Analytics":
        "Interactive charts, trend analysis and visual exploration.",

    "🤖 Prediction Center":
        "Goal prediction and calorie prediction using trained ML models.",

    "🧠 AI Coach":
        "Personalized recommendations and wellness assessment.",

    "📄 Reports":
        "Generate summaries and download AI-generated reports.",

    "ℹ️ About":
        "Project information, technologies and future scope."
}

for module, description in modules.items():
    st.write(f"**{module}**")
    st.caption(description)

st.divider()
# ---------------------------------------------------
# SYSTEM ARCHITECTURE
# ---------------------------------------------------

st.subheader("🏗 System Architecture")

st.code("""
                Fitbit Dataset
                      │
                      ▼
             Data Loading (Pandas)
                      │
                      ▼
             Data Cleaning & Validation
                      │
                      ▼
             Feature Engineering
                      │
                      ▼
      ┌─────────────────────────────┐
      │ Machine Learning Models     │
      │                             │
      │ Random Forest Classifier    │
      │ Random Forest Regressor     │
      └─────────────────────────────┘
                      │
                      ▼
                 FastAPI Backend
                      │
                      ▼
             Streamlit Dashboard
                      │
                      ▼
     Analytics • Predictions • Reports
""")

st.divider()

# ---------------------------------------------------
# MACHINE LEARNING MODELS
# ---------------------------------------------------

st.subheader("🤖 Machine Learning Models")

import pandas as pd

models = pd.DataFrame({

    "Model":[
        "Goal Achievement Prediction",
        "Calorie Prediction"
    ],

    "Algorithm":[
        "Random Forest Classifier",
        "Random Forest Regressor"
    ],

    "Purpose":[
        "Predict whether a user achieves the daily step goal",
        "Predict calories burned from activity data"
    ]

})

st.dataframe(
    models,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ---------------------------------------------------
# TECHNOLOGY STACK
# ---------------------------------------------------

st.subheader("⚙ Technology Stack")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.success("""
### 🐍 Python

Core Programming Language
""")

    st.info("""
### 📊 Pandas

Data Analysis
""")

with col2:

    st.success("""
### ⚡ FastAPI

REST API Backend
""")

    st.info("""
### 🤖 Scikit-Learn

Machine Learning
""")

with col3:

    st.success("""
### 🎨 Streamlit

Frontend Dashboard
""")

    st.info("""
### 📈 Plotly

Interactive Charts
""")

with col4:

    st.success("""
### 💾 Joblib

Model Serialization
""")

    st.info("""
### 📂 CSV Dataset

Fitbit Activity Dataset
""")

st.divider()

# ---------------------------------------------------
# PROJECT WORKFLOW
# ---------------------------------------------------

st.subheader("🔄 Project Workflow")

workflow = pd.DataFrame({

    "Step":[
        "1",
        "2",
        "3",
        "4",
        "5",
        "6"
    ],

    "Process":[
        "Load Fitbit Dataset",
        "Clean & Validate Data",
        "Feature Engineering",
        "Train Machine Learning Models",
        "Deploy using FastAPI",
        "Visualize using Streamlit"
    ]

})

st.dataframe(
    workflow,
    use_container_width=True,
    hide_index=True
)

st.divider()
# ---------------------------------------------------
# FUTURE SCOPE
# ---------------------------------------------------

st.subheader("🚀 Future Scope")

future1, future2 = st.columns(2)

with future1:

    st.success("""
✔ Fitbit API Integration

Automatically synchronize fitness data
from wearable devices.
""")

    st.success("""
✔ Google Fit Integration

Import daily activity directly
from Google Fit.
""")

    st.success("""
✔ Apple Health Support

Cross-platform health data
integration.
""")

    st.success("""
✔ Heart Rate Monitoring

Real-time heart rate
analytics.
""")

with future2:

    st.success("""
✔ Deep Learning Models

Improve prediction accuracy
using Neural Networks.
""")

    st.success("""
✔ Mobile Application

Android & iOS version
of FitIntel AI.
""")

    st.success("""
✔ Cloud Deployment

Deploy on AWS,
Azure or Google Cloud.
""")

    st.success("""
✔ AI Chat Assistant

LLM-powered personalized
fitness coaching.
""")

st.divider()

# ---------------------------------------------------
# PROJECT STATISTICS
# ---------------------------------------------------

st.subheader("📊 Project Statistics")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "ML Models",
    "2"
)

c2.metric(
    "REST APIs",
    "2"
)

c3.metric(
    "Dashboard Pages",
    "6"
)

c4.metric(
    "Dataset Records",
    "940"
)

st.divider()

# ---------------------------------------------------
# PROJECT HIGHLIGHTS
# ---------------------------------------------------

st.subheader("🏆 Project Highlights")

st.markdown("""
- ✅ Interactive Analytics Dashboard

- ✅ Machine Learning Predictions

- ✅ Goal Achievement Prediction

- ✅ Calorie Burn Prediction

- ✅ AI Fitness Coach

- ✅ Downloadable Reports

- ✅ FastAPI REST APIs

- ✅ Interactive Plotly Visualizations

- ✅ Responsive Streamlit Interface

- ✅ Modular Project Architecture
""")

st.divider()

# ---------------------------------------------------
# DEVELOPER
# ---------------------------------------------------

st.subheader("👩‍💻 Developer")

developer1, developer2 = st.columns([1,2])

with developer1:

    st.info("""
## 👩

**Thejaswini S**

B.E Artificial Intelligence & Machine Learning

K. Ramakrishnan College of Engineering
""")

with developer2:

    st.write("""
### About the Developer

FitIntel AI was developed as an academic Machine Learning project
to demonstrate practical implementation of Artificial Intelligence,
Data Analytics and Web Development.

The project combines:

- Machine Learning

- Data Visualization

- REST API Development

- Interactive Dashboards

- AI-based Recommendations

The primary objective is to transform raw fitness data into
meaningful insights that help users understand and improve
their daily health habits.
""")

st.divider()

# ---------------------------------------------------
# VERSION INFORMATION
# ---------------------------------------------------

st.subheader("📦 Version Information")

version = {
    "Application": "FitIntel AI",
    "Version": "1.0",
    "Release Year": "2026",
    "Backend": "FastAPI",
    "Frontend": "Streamlit",
    "Machine Learning": "Scikit-Learn",
    "Visualization": "Plotly",
    "Programming Language": "Python"
}

version_df = pd.DataFrame(
    version.items(),
    columns=["Component", "Details"]
)

st.dataframe(
    version_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ---------------------------------------------------
# ACKNOWLEDGEMENT
# ---------------------------------------------------

st.subheader("🙏 Acknowledgement")

st.info("""
This project uses the Fitbit Daily Activity Dataset for educational
purposes to demonstrate the practical application of Machine Learning,
Data Analytics, Data Visualization, and AI-driven decision support.
""")

st.divider()

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown(
"""
---
<div style='text-align:center;'>

<h2>💪 FitIntel AI</h2>

<p><strong>AI-Powered Fitness Analytics Platform</strong></p>

<p>
Python • FastAPI • Streamlit • Plotly • Scikit-Learn
</p>

<p>
Developed by <strong>Thejaswini S</strong>
</p>

<p>
Version 1.0 • © 2026
</p>

</div>
""",
unsafe_allow_html=True
)