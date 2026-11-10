import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# LOAD CSS
# ---------------------------------------------------

def load_css():
    with open("dashboard/assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/raw/dailyActivity_merged.csv"
    )

    df["ActivityDate"] = pd.to_datetime(
        df["ActivityDate"]
    )

    return df

df = load_data()

# ---------------------------------------------------
# ACTIVITY LEVEL
# ---------------------------------------------------

def activity_level(steps):

    if steps >= 12000:
        return "Highly Active"

    elif steps >= 10000:
        return "Active"

    elif steps >= 7500:
        return "Moderately Active"

    return "Low Active"

df["ActivityLevel"] = df["TotalSteps"].apply(
    activity_level
)

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------

st.sidebar.title("📌 Filters")

activity_filter = st.sidebar.multiselect(
    "Activity Level",
    options=df["ActivityLevel"].unique(),
    default=df["ActivityLevel"].unique()
)

filtered_df = df[
    df["ActivityLevel"].isin(activity_filter)
]

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
"""
<div class='main-title'>
📊 Executive Dashboard
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='sub-title'>
Interactive Fitness Analytics
</div>
""",
unsafe_allow_html=True
)

st.write("")

# ---------------------------------------------------
# KPI VALUES
# ---------------------------------------------------

records = len(filtered_df)

avg_steps = int(
    filtered_df["TotalSteps"].mean()
)

avg_calories = int(
    filtered_df["Calories"].mean()
)

avg_distance = round(
    filtered_df["TotalDistance"].mean(),
    2
)

goal_rate = round(
(
(filtered_df["TotalSteps"] >= 10000).sum()
/
len(filtered_df)
)*100,
2
)

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.markdown(f"""
<div class='card'>

<div class='card-title'>
👥 Records
</div>

<div class='card-value'>
{records}
</div>

</div>
""",unsafe_allow_html=True)

with c2:

    st.markdown(f"""
<div class='card'>

<div class='card-title'>
🚶 Avg Steps
</div>

<div class='card-value'>
{avg_steps:,}
</div>

</div>
""",unsafe_allow_html=True)

with c3:

    st.markdown(f"""
<div class='card'>

<div class='card-title'>
🔥 Avg Calories
</div>

<div class='card-value'>
{avg_calories:,}
</div>

</div>
""",unsafe_allow_html=True)

with c4:

    st.markdown(f"""
<div class='card'>

<div class='card-title'>
🎯 Goal Rate
</div>

<div class='card-value'>
{goal_rate}%
</div>

</div>
""",unsafe_allow_html=True)

st.write("")

# ---------------------------------------------------
# FIRST ROW OF CHARTS
# ---------------------------------------------------

left,right = st.columns(2)

with left:

    fig = px.line(

        filtered_df,

        x="ActivityDate",

        y="TotalSteps",

        markers=True,

        template="plotly_white",

        title="📈 Daily Steps Trend"
    )

    fig.update_layout(
        height=380,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    activity = (
        filtered_df["ActivityLevel"]
        .value_counts()
        .reset_index()
    )

    activity.columns=[
        "Activity",
        "Count"
    ]

    fig = px.pie(

        activity,

        names="Activity",

        values="Count",

        hole=.55,

        template="plotly_white",

        title="🥧 Activity Distribution"
    )

    fig.update_layout(
        height=380
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
# ---------------------------------------------------
# SECOND ROW OF CHARTS
# ---------------------------------------------------

left, right = st.columns(2)

with left:

    fig = px.scatter(
        filtered_df,
        x="TotalSteps",
        y="Calories",
        color="ActivityLevel",
        size="TotalDistance",
        hover_data=["ActivityDate"],
        title="🔥 Steps vs Calories",
        template="plotly_white"
    )

    fig.update_layout(
        height=380,
        margin=dict(l=20, r=20, t=60, b=20)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    corr = filtered_df[
        [
            "TotalSteps",
            "Calories",
            "TotalDistance",
            "VeryActiveMinutes",
            "SedentaryMinutes"
        ]
    ].corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="Blues",
        title="🔥 Correlation Heatmap",
        aspect="auto"
    )

    fig.update_layout(
        height=380
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.write("")
# ---------------------------------------------------
# THIRD ROW
# ---------------------------------------------------

left, right = st.columns(2)

with left:

    fig = px.box(
        filtered_df,
        y="Calories",
        color="ActivityLevel",
        title="📦 Calories Distribution",
        template="plotly_white"
    )

    fig.update_layout(
        height=380
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    avg = (
        filtered_df
        .groupby("ActivityLevel")["Calories"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        avg,
        x="ActivityLevel",
        y="Calories",
        color="ActivityLevel",
        text_auto=".0f",
        title="📊 Average Calories by Activity Level",
        template="plotly_white"
    )

    fig.update_layout(
        height=380,
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.write("")
# ---------------------------------------------------
# GOAL ACHIEVEMENT
# ---------------------------------------------------

st.subheader("🎯 Goal Achievement")

fig = go.Figure(go.Indicator(

    mode="gauge+number",

    value=goal_rate,

    number={"suffix":"%"},

    title={"text":"Goal Achievement"},

    gauge={

        "axis":{"range":[0,100]},

        "bar":{"color":"royalblue"},

        "steps":[

            {"range":[0,40],"color":"#FECACA"},

            {"range":[40,70],"color":"#FDE68A"},

            {"range":[70,100],"color":"#BBF7D0"}

        ]
    }

))

fig.update_layout(height=320)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.write("")
# ---------------------------------------------------
# AI HEALTH SUMMARY
# ---------------------------------------------------

st.markdown(
"""
<div class='ai-card'>

<h2>🤖 AI Health Summary</h2>

</div>
""",
unsafe_allow_html=True
)

avg_sedentary = filtered_df["SedentaryMinutes"].mean()

if avg_steps < 10000:

    st.warning(
        f"🚶 Average daily steps are {avg_steps:,}. Increase by {10000-avg_steps:,} steps to reach the recommended goal."
    )

else:

    st.success(
        "Excellent daily step count!"
    )

if avg_sedentary > 800:

    st.warning(
        "🪑 Sedentary time is high. Consider taking a short walk every hour."
    )

else:

    st.success(
        "Sedentary time is within a healthy range."
    )

if avg_calories > 2000:

    st.success(
        f"🔥 Average calorie burn is {avg_calories:,} kcal/day."
    )

else:

    st.info(
        "Increase physical activity to burn more calories."
    )

st.info(
    "💡 Consistent exercise, better sleep and lower sedentary time will improve overall fitness."
)

st.divider()
st.markdown(
"""
<div style="text-align:center;color:gray;padding:15px;">

Developed by <b>Thejaswini S</b><br>

FitIntel AI • AI Powered Fitness Analytics Platform

</div>
""",
unsafe_allow_html=True
)