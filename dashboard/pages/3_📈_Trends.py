import streamlit as st
import pandas as pd
import plotly.express as px


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Trends | FitIntel AI",
    page_icon="📈",
    layout="wide"
)


# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():

    try:

        with open("dashboard/assets/style.css", encoding="utf-8") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    except FileNotFoundError:

        pass


load_css()


# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/raw/dailyActivity_merged.csv"
    )

    df["ActivityDate"] = pd.to_datetime(
        df["ActivityDate"]
    )

    df = df.sort_values(
        "ActivityDate"
    )

    return df


df = load_data()


# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    """
    <div class="main-title">
        📈 Fitness Trends
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sub-title">
        Understand how your fitness activity changes over time
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")


# ==========================================================
# INTRO CARD
# ==========================================================

st.markdown(
    """
    <div class="ai-card">
        <h2>📊 Track Your Fitness Journey</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="font-size:15px; line-height:1.7;">
        Analyze your daily steps, calorie burn, distance and
        activity levels to understand long-term fitness patterns.
    </p>
    """,
    unsafe_allow_html=True
)

st.write("")


# ==========================================================
# DATE FILTER
# ==========================================================

st.subheader("📅 Time Period")

min_date = df["ActivityDate"].min().date()

max_date = df["ActivityDate"].max().date()

date_range = st.date_input(
    "Select date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if isinstance(date_range, tuple) and len(date_range) == 2:

    start_date, end_date = date_range

    trend_df = df[
        (df["ActivityDate"].dt.date >= start_date)
        &
        (df["ActivityDate"].dt.date <= end_date)
    ].copy()

else:

    trend_df = df.copy()


st.divider()


# ==========================================================
# EMPTY DATA CHECK
# ==========================================================

if trend_df.empty:

    st.warning(
        "No fitness records are available for the selected date range."
    )

    st.stop()


# ==========================================================
# KPI SUMMARY
# ==========================================================

st.subheader("📌 Trend Summary")

c1, c2, c3, c4 = st.columns(4)


with c1:

    st.metric(
        "🚶 Avg Steps",
        f"{trend_df['TotalSteps'].mean():,.0f}"
    )


with c2:

    st.metric(
        "🔥 Avg Calories",
        f"{trend_df['Calories'].mean():,.0f}"
    )


with c3:

    st.metric(
        "📏 Avg Distance",
        f"{trend_df['TotalDistance'].mean():.2f} km"
    )


with c4:

    st.metric(
        "📋 Records",
        f"{len(trend_df):,}"
    )


st.write("")


# ==========================================================
# STEPS TREND
# ==========================================================

st.subheader("🚶 Daily Steps Trend")

fig_steps = px.line(
    trend_df,
    x="ActivityDate",
    y="TotalSteps",
    markers=True,
    title="Daily Steps",
    template="plotly_white"
)

fig_steps.add_hline(
    y=10000,
    line_dash="dash",
    annotation_text="10,000 Step Goal",
    annotation_position="top left"
)

fig_steps.update_layout(
    height=430,
    xaxis_title="Date",
    yaxis_title="Steps",
    margin=dict(
        l=20,
        r=20,
        t=60,
        b=20
    )
)

st.plotly_chart(
    fig_steps,
    width="stretch"
)


st.divider()


# ==========================================================
# CALORIES TREND
# ==========================================================

st.subheader("🔥 Daily Calorie Trend")

fig_calories = px.line(
    trend_df,
    x="ActivityDate",
    y="Calories",
    markers=True,
    title="Calories Burned",
    template="plotly_white"
)

fig_calories.update_layout(
    height=430,
    xaxis_title="Date",
    yaxis_title="Calories",
    margin=dict(
        l=20,
        r=20,
        t=60,
        b=20
    )
)

st.plotly_chart(
    fig_calories,
    width="stretch"
)


st.divider()


# ==========================================================
# DISTANCE TREND
# ==========================================================

st.subheader("📏 Distance Trend")

fig_distance = px.area(
    trend_df,
    x="ActivityDate",
    y="TotalDistance",
    title="Daily Distance",
    template="plotly_white"
)

fig_distance.update_layout(
    height=400,
    xaxis_title="Date",
    yaxis_title="Distance (km)",
    margin=dict(
        l=20,
        r=20,
        t=60,
        b=20
    )
)

st.plotly_chart(
    fig_distance,
    width="stretch"
)


st.divider()


# ==========================================================
# ACTIVITY MINUTES
# ==========================================================

st.subheader("💪 Activity Minutes")

activity_columns = [
    "VeryActiveMinutes",
    "FairlyActiveMinutes",
    "LightlyActiveMinutes",
    "SedentaryMinutes"
]

activity_data = trend_df[
    ["ActivityDate"] + activity_columns
].melt(
    id_vars="ActivityDate",
    var_name="Activity Type",
    value_name="Minutes"
)

fig_activity = px.line(
    activity_data,
    x="ActivityDate",
    y="Minutes",
    color="Activity Type",
    title="Daily Activity Minutes",
    template="plotly_white"
)

fig_activity.update_layout(
    height=450,
    xaxis_title="Date",
    yaxis_title="Minutes",
    margin=dict(
        l=20,
        r=20,
        t=60,
        b=20
    )
)

st.plotly_chart(
    fig_activity,
    width="stretch"
)


st.divider()


# ==========================================================
# WEEKLY ANALYSIS
# ==========================================================

st.subheader("📅 Weekly Fitness Analysis")

weekly_df = trend_df.copy()

weekly_df["Week"] = (
    weekly_df["ActivityDate"]
    .dt.to_period("W")
    .astype(str)
)

weekly = (
    weekly_df
    .groupby("Week")
    .agg(
        Steps=("TotalSteps", "mean"),
        Calories=("Calories", "mean"),
        Distance=("TotalDistance", "mean")
    )
    .reset_index()
)


left, right = st.columns(2)


with left:

    fig_week_steps = px.bar(
        weekly,
        x="Week",
        y="Steps",
        title="Average Steps by Week",
        template="plotly_white"
    )

    fig_week_steps.add_hline(
        y=10000,
        line_dash="dash",
        annotation_text="10,000 Goal"
    )

    fig_week_steps.update_layout(
        height=400,
        xaxis_title="Week",
        yaxis_title="Average Steps"
    )

    st.plotly_chart(
        fig_week_steps,
        width="stretch"
    )


with right:

    fig_week_calories = px.bar(
        weekly,
        x="Week",
        y="Calories",
        title="Average Calories by Week",
        template="plotly_white"
    )

    fig_week_calories.update_layout(
        height=400,
        xaxis_title="Week",
        yaxis_title="Average Calories"
    )

    st.plotly_chart(
        fig_week_calories,
        width="stretch"
    )


st.divider()


# ==========================================================
# ACTIVITY LEVEL CLASSIFICATION
# ==========================================================

def activity_level(steps):

    if steps >= 12000:

        return "Highly Active"

    elif steps >= 10000:

        return "Active"

    elif steps >= 7500:

        return "Moderately Active"

    else:

        return "Low Active"


trend_df["ActivityLevel"] = (
    trend_df["TotalSteps"]
    .apply(activity_level)
)


st.subheader("🏃 Activity Level Distribution")


activity_counts = (
    trend_df["ActivityLevel"]
    .value_counts()
    .reset_index()
)


activity_counts.columns = [
    "Activity Level",
    "Records"
]


fig_levels = px.bar(
    activity_counts,
    x="Activity Level",
    y="Records",
    text="Records",
    title="Number of Records by Activity Level",
    template="plotly_white"
)

fig_levels.update_layout(
    height=400,
    xaxis_title="Activity Level",
    yaxis_title="Number of Records"
)

st.plotly_chart(
    fig_levels,
    width="stretch"
)


st.divider()


# ==========================================================
# BEST & WORST DAYS
# ==========================================================

st.subheader("🏆 Fitness Highlights")

best_day = trend_df.loc[
    trend_df["TotalSteps"].idxmax()
]

worst_day = trend_df.loc[
    trend_df["TotalSteps"].idxmin()
]


c1, c2 = st.columns(2)


with c1:

    st.success(
        f"""
🏆 **Best Activity Day**

Date: **{best_day['ActivityDate'].strftime('%d %b %Y')}**

Steps: **{best_day['TotalSteps']:,}**

Calories: **{best_day['Calories']:,}**

Distance: **{best_day['TotalDistance']:.2f} km**
"""
    )


with c2:

    st.warning(
        f"""
📉 **Lowest Activity Day**

Date: **{worst_day['ActivityDate'].strftime('%d %b %Y')}**

Steps: **{worst_day['TotalSteps']:,}**

Calories: **{worst_day['Calories']:,}**

Distance: **{worst_day['TotalDistance']:.2f} km**
"""
    )


st.divider()


# ==========================================================
# FITNESS INSIGHT
# ==========================================================

st.subheader("🤖 Trend Insight")

goal_days = (
    trend_df["TotalSteps"] >= 10000
).sum()

total_records = len(trend_df)

goal_percentage = (
    goal_days / total_records * 100
    if total_records > 0
    else 0
)


if goal_percentage >= 70:

    st.success(
        f"""
🎯 **Excellent consistency!**

You achieved the 10,000-step goal on
**{goal_percentage:.1f}%** of the selected records.
"""
    )

elif goal_percentage >= 40:

    st.info(
        f"""
📈 **Moderate consistency.**

You achieved the 10,000-step goal on
**{goal_percentage:.1f}%** of the selected records.

Try to build a more consistent daily routine.
"""
    )

else:

    st.warning(
        f"""
🚶 **Your activity consistency can improve.**

Only **{goal_percentage:.1f}%** of the selected records
reached the 10,000-step goal.
"""
    )


st.divider()


# ==========================================================
# DATA TABLE
# ==========================================================

with st.expander("📋 View Trend Data"):

    st.dataframe(
        trend_df,
        width="stretch",
        hide_index=True
    )


st.divider()


# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
    """
    <div style="text-align:center; color:gray; padding:20px;">
        <b>💪 FitIntel AI</b><br>
        AI-Powered Fitness Analytics Platform<br>
        Developed by <b>Thejaswini S</b><br>
        B.E Computer Science & Engineering (AI & ML)
    </div>
    """,
    unsafe_allow_html=True
)