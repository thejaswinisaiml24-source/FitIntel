import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("data/raw/dailyActivity_merged.csv")
    df["ActivityDate"] = pd.to_datetime(df["ActivityDate"])
    return df

df = load_data()

# --------------------------------------------------
# ACTIVITY LEVEL
# --------------------------------------------------

def activity_level(steps):

    if steps >= 12000:
        return "Highly Active"

    elif steps >= 10000:
        return "Active"

    elif steps >= 7500:
        return "Moderately Active"

    else:
        return "Low Active"

df["ActivityLevel"] = df["TotalSteps"].apply(activity_level)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🎛 Dashboard Filters")

activity = st.sidebar.multiselect(

    "Activity Level",

    df["ActivityLevel"].unique(),

    default=df["ActivityLevel"].unique()

)

minimum_steps = st.sidebar.slider(

    "Minimum Steps",

    0,

    20000,

    0

)

filtered = df[
    (df["ActivityLevel"].isin(activity))
    &
    (df["TotalSteps"] >= minimum_steps)
]

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📈 FitIntel AI Analytics Dashboard")

st.caption(
    "Interactive AI-powered Fitness Analytics"
)

st.divider()

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

goal_rate = (
    (filtered["TotalSteps"] >= 10000).sum()
    /
    len(filtered)
) * 100

k1,k2,k3,k4,k5 = st.columns(5)

k1.metric(
    "📄 Records",
    len(filtered)
)

k2.metric(
    "🚶 Avg Steps",
    f"{int(filtered.TotalSteps.mean()):,}"
)

k3.metric(
    "🔥 Avg Calories",
    f"{int(filtered.Calories.mean())}"
)

k4.metric(
    "📏 Avg Distance",
    f"{filtered.TotalDistance.mean():.2f} km"
)

k5.metric(
    "🎯 Goal %",
    f"{goal_rate:.1f}%"
)

st.divider()
# --------------------------------------------------
# FIRST ROW
# --------------------------------------------------

left, right = st.columns(2)

# ---------------- Daily Steps ----------------

with left:

    fig = px.line(

        filtered,

        x="ActivityDate",

        y="TotalSteps",

        markers=True,

        title="📈 Daily Steps Trend",

        template="plotly_white"

    )

    fig.update_layout(

        height=340,

        margin=dict(l=10,r=10,t=45,b=10)

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

# ---------------- Activity Distribution ----------------

with right:

    activity_df = (

        filtered["ActivityLevel"]

        .value_counts()

        .reset_index()

    )

    activity_df.columns = [

        "Activity",

        "Count"

    ]

    fig = px.pie(

        activity_df,

        names="Activity",

        values="Count",

        hole=0.55,

        title="🥧 Activity Distribution",

        template="plotly_white"

    )

    fig.update_layout(

        height=340,

        margin=dict(l=10,r=10,t=45,b=10)

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

# --------------------------------------------------
# SECOND ROW
# --------------------------------------------------

left, right = st.columns(2)

# ---------------- Scatter ----------------

with left:

    fig = px.scatter(

        filtered,

        x="TotalSteps",

        y="Calories",

        color="Calories",

        size="TotalDistance",

        hover_data=["ActivityDate"],

        title="🔥 Steps vs Calories",

        template="plotly_white"

    )

    fig.update_layout(

        height=340,

        margin=dict(l=10,r=10,t=45,b=10)

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

# ---------------- Calories ----------------

with right:

    calories = (

        filtered

        .groupby("ActivityLevel")["Calories"]

        .mean()

        .reset_index()

    )

    fig = px.bar(

        calories,

        x="ActivityLevel",

        y="Calories",

        color="ActivityLevel",

        title="📊 Average Calories",

        template="plotly_white"

    )

    fig.update_layout(

        showlegend=False,

        height=340,

        margin=dict(l=10,r=10,t=45,b=10)

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

st.divider()
# --------------------------------------------------
# THIRD ROW
# --------------------------------------------------

left, right = st.columns(2)

# ---------------- Goal Achievement Gauge ----------------

with left:

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=goal_rate,

        title={"text":"🎯 Goal Achievement (%)"},

        gauge={

            "axis":{"range":[0,100]},

            "bar":{"color":"royalblue"},

            "steps":[

                {"range":[0,40],"color":"#F8B4B4"},

                {"range":[40,70],"color":"#FDE68A"},

                {"range":[70,100],"color":"#86EFAC"}

            ]

        }

    ))

    fig.update_layout(

        height=340,

        margin=dict(l=10,r=10,t=45,b=10)

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

# ---------------- Histogram ----------------

with right:

    fig = px.histogram(

        filtered,

        x="TotalSteps",

        nbins=25,

        title="📦 Daily Steps Distribution",

        template="plotly_white"

    )

    fig.update_layout(

        height=340,

        margin=dict(l=10,r=10,t=45,b=10)

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

st.divider()

# --------------------------------------------------
# CORRELATION HEATMAP
# --------------------------------------------------

st.subheader("🔥 Feature Correlation")

corr = filtered[
    [
        "TotalSteps",
        "Calories",
        "TotalDistance",
        "VeryActiveMinutes",
        "FairlyActiveMinutes",
        "LightlyActiveMinutes",
        "SedentaryMinutes"
    ]
].corr()

fig = px.imshow(

    corr,

    text_auto=".2f",

    color_continuous_scale="RdBu_r",

    aspect="auto",

    title="Correlation Matrix"

)

fig.update_layout(

    height=500,

    margin=dict(l=10,r=10,t=50,b=10)

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()
# --------------------------------------------------
# AI INSIGHTS
# --------------------------------------------------

st.subheader("🤖 AI Insights")

col1, col2 = st.columns(2)

with col1:

    avg_steps = filtered["TotalSteps"].mean()
    avg_calories = filtered["Calories"].mean()
    avg_distance = filtered["TotalDistance"].mean()
    avg_sedentary = filtered["SedentaryMinutes"].mean()

    if avg_steps >= 10000:
        st.success("✅ Excellent daily activity level.")
    elif avg_steps >= 7500:
        st.info("👍 Good activity level. You're close to the recommended goal.")
    else:
        st.warning("⚠ Increase your daily walking activity.")

    if avg_sedentary > 800:
        st.warning("🪑 High sedentary time detected.")
    else:
        st.success("🚶 Healthy sedentary time.")

    if avg_calories >= 2200:
        st.success("🔥 Healthy calorie expenditure.")
    else:
        st.info("🍎 Increasing physical activity may improve calorie burn.")

with col2:

    st.markdown("### 💡 AI Recommendations")

    recommendations = []

    if avg_steps < 10000:
        recommendations.append(
            "🚶 Walk 30–45 minutes daily."
        )

    if avg_sedentary > 800:
        recommendations.append(
            "🪑 Stand and stretch every hour."
        )

    if avg_distance < 6:
        recommendations.append(
            "📏 Increase walking distance."
        )

    if avg_calories < 2200:
        recommendations.append(
            "🔥 Include moderate exercise."
        )

    if len(recommendations) == 0:
        st.success("🎉 Excellent! No major improvements needed.")

    else:
        for item in recommendations:
            st.write(item)

st.divider()

# --------------------------------------------------
# QUICK STATISTICS
# --------------------------------------------------

st.subheader("📊 Quick Statistics")

stats1, stats2, stats3, stats4 = st.columns(4)

stats1.metric(
    "Highest Steps",
    f"{int(filtered['TotalSteps'].max()):,}"
)

stats2.metric(
    "Lowest Steps",
    f"{int(filtered['TotalSteps'].min()):,}"
)

stats3.metric(
    "Highest Calories",
    int(filtered["Calories"].max())
)

stats4.metric(
    "Longest Distance",
    f"{filtered['TotalDistance'].max():.2f} km"
)

st.divider()

# --------------------------------------------------
# DATASET PREVIEW
# --------------------------------------------------

with st.expander("📄 Dataset Preview", expanded=False):

    st.dataframe(
        filtered,
        use_container_width=True,
        height=350
    )

st.divider()

# --------------------------------------------------
# DATASET SUMMARY
# --------------------------------------------------

with st.expander("📋 Dataset Summary", expanded=False):

    st.dataframe(
        filtered.describe().round(2),
        use_container_width=True
    )

st.divider()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
"""
---
<div style='text-align:center'>

## 💪 FitIntel AI Analytics

Interactive Fitness Analytics Dashboard

Built using

🐍 Python • ⚡ FastAPI • 🎨 Streamlit • 📊 Plotly • 🤖 Machine Learning

Developed by **Thejaswini S**

Version **1.0**

</div>
""",
unsafe_allow_html=True
)