import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import random


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Coach",
    page_icon="🧠",
    layout="wide"
)


# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():
    try:
        with open("dashboard/assets/style.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except Exception:
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

    return df


df = load_data()


# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    """
    <div class="main-title">
        🧠 AI Fitness Coach
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sub-title">
        Your Personal AI Health Assistant
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

st.success(
    "Receive personalized fitness insights generated from your activity data."
)

st.divider()


# ==========================================================
# USER INPUTS
# ==========================================================

st.subheader("🏃 Today's Activity")

c1, c2, c3 = st.columns(3)


with c1:

    steps = st.slider(
        "👣 Steps",
        0,
        30000,
        8500
    )

    distance = st.slider(
        "📏 Distance (km)",
        0.0,
        25.0,
        6.2,
        0.1
    )


with c2:

    calories = st.slider(
        "🔥 Calories",
        1000,
        5000,
        2200
    )

    active = st.slider(
        "💪 Very Active Minutes",
        0,
        180,
        35
    )


with c3:

    sedentary = st.slider(
        "🪑 Sedentary Minutes",
        0,
        1440,
        650
    )

    water = st.slider(
        "💧 Water Intake (Litres)",
        0.0,
        5.0,
        2.2,
        0.1
    )


st.divider()


# ==========================================================
# FITNESS SCORE
# ==========================================================

score = 0


# Steps
if steps >= 10000:
    score += 25
elif steps >= 7500:
    score += 18
else:
    score += 10


# Calories
if calories >= 2200:
    score += 20
else:
    score += 12


# Active minutes
if active >= 30:
    score += 20
else:
    score += 10


# Sedentary time
if sedentary <= 700:
    score += 20
else:
    score += 8


# Hydration
if water >= 2.5:
    score += 15
else:
    score += 8


score = min(score, 100)


# ==========================================================
# SCORE CARD
# ==========================================================

left, right = st.columns([1, 2])


with left:

    fig = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=score,

            title={
                "text": "Fitness Score"
            },

            gauge={

                "axis": {
                    "range": [0, 100]
                },

                "bar": {
                    "color": "royalblue"
                },

                "steps": [

                    {
                        "range": [0, 40],
                        "color": "#FCA5A5"
                    },

                    {
                        "range": [40, 70],
                        "color": "#FDE68A"
                    },

                    {
                        "range": [70, 100],
                        "color": "#86EFAC"
                    }

                ]
            }

        )
    )

    fig.update_layout(
        height=330
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


with right:

    st.subheader(
        "📊 Today's Health Summary"
    )

    m1, m2 = st.columns(2)


    with m1:

        st.metric(
            "👣 Steps",
            f"{steps:,}"
        )

        st.metric(
            "🔥 Calories",
            calories
        )


    with m2:

        st.metric(
            "💧 Water",
            f"{water:.1f} L"
        )

        st.metric(
            "💪 Active",
            f"{active} min"
        )


    st.progress(
        score / 100
    )

    st.write(
        f"Overall Fitness Score : **{score}/100**"
    )


# ==========================================================
# AI HEALTH ANALYSIS
# ==========================================================

st.divider()

st.subheader(
    "🤖 AI Health Analysis"
)

left, right = st.columns(2)


# ==========================================================
# STEP + CALORIE ANALYSIS
# ==========================================================

with left:

    st.markdown(
        "### 🚶 Step Analysis"
    )


    if steps >= 12000:

        st.success(
            "Excellent! Your daily step count is outstanding."
        )

    elif steps >= 10000:

        st.success(
            "Great! You achieved the recommended 10,000 daily steps."
        )

    elif steps >= 7500:

        st.warning(
            "You're close to the recommended goal. Try walking a little more."
        )

    else:

        st.error(
            "Your step count is low today. Aim for at least 10,000 steps."
        )


    st.progress(
        min(steps / 10000, 1.0)
    )

    st.write(
        f"Progress toward goal: **{steps:,} / 10,000 steps**"
    )


    st.markdown("---")


    st.markdown(
        "### 🔥 Calorie Analysis"
    )


    if calories >= 2800:

        st.success(
            "High calorie burn indicates excellent physical activity."
        )

    elif calories >= 2200:

        st.info(
            "Your calorie burn is within a healthy range."
        )

    else:

        st.warning(
            "Increase daily activity to improve calorie expenditure."
        )


# ==========================================================
# HYDRATION + SEDENTARY ANALYSIS
# ==========================================================

with right:

    st.markdown(
        "### 💧 Hydration"
    )


    if water >= 3.0:

        st.success(
            "Excellent hydration level."
        )

    elif water >= 2.5:

        st.info(
            "Good hydration. Keep drinking water regularly."
        )

    else:

        st.warning(
            "Drink more water to stay hydrated."
        )


    st.progress(
        min(water / 3.0, 1.0)
    )

    st.write(
        f"Today's Water Intake : **{water:.1f} L**"
    )


    st.markdown("---")


    st.markdown(
        "### 🪑 Sedentary Analysis"
    )


    if sedentary <= 600:

        st.success(
            "Excellent! You stayed active throughout the day."
        )

    elif sedentary <= 800:

        st.info(
            "Moderate sedentary time."
        )

    else:

        st.error(
            "High sedentary time detected. Stand up and walk every hour."
        )


st.divider()


# ==========================================================
# OVERALL HEALTH STATUS
# ==========================================================

st.subheader(
    "🩺 Overall Health Status"
)


if score >= 90:

    st.success(
        "🌟 Excellent! Your overall fitness is outstanding today."
    )

elif score >= 75:

    st.success(
        "✅ Good fitness level. Keep maintaining your routine."
    )

elif score >= 60:

    st.warning(
        "⚠ Moderate fitness. Small improvements can make a big difference."
    )

else:

    st.error(
        "❌ Your activity level is low today. Increase movement and reduce sedentary time."
    )


st.divider()


# ==========================================================
# PERSONALIZED AI RECOMMENDATIONS
# ==========================================================

st.subheader(
    "🧠 Personalized AI Recommendations"
)


recommendations = []


# Steps
if steps < 10000:

    recommendations.append(
        f"🚶 Walk another **{10000 - steps:,} steps** to reach today's goal."
    )

else:

    recommendations.append(
        "🏆 Excellent! You have already achieved today's step goal."
    )


# Active Minutes
if active < 30:

    recommendations.append(
        "💪 Add 15–20 minutes of brisk walking or exercise."
    )

else:

    recommendations.append(
        "🔥 Great job maintaining your active minutes."
    )


# Water
if water < 2.5:

    recommendations.append(
        f"💧 Drink approximately **{2.5 - water:.1f} L** more water today."
    )

else:

    recommendations.append(
        "💧 Your hydration level is excellent."
    )


# Sedentary
if sedentary > 800:

    recommendations.append(
        "🪑 Stand up and walk for 5 minutes every hour."
    )

else:

    recommendations.append(
        "🚶 Nice! Your sedentary time is under control."
    )


# Calories
if calories < 2200:

    recommendations.append(
        "🔥 Increase physical activity to improve calorie burn."
    )

else:

    recommendations.append(
        "🔥 Healthy calorie expenditure detected."
    )


for tip in recommendations:

    st.info(tip)


st.divider()


# ==========================================================
# WEEKLY FITNESS CHALLENGE
# ==========================================================

st.subheader(
    "🏅 Weekly Fitness Challenge"
)


challenge_progress = min(
    (steps / 12000) * 100,
    100
)


st.progress(
    challenge_progress / 100
)


st.write(
    f"Today's Progress: **{challenge_progress:.1f}%**"
)


if challenge_progress >= 100:

    st.success(
        "🏆 Challenge Completed! Fantastic work today."
    )

elif challenge_progress >= 75:

    st.info(
        "💪 Almost there! A little more walking will complete today's challenge."
    )

else:

    st.warning(
        "🚶 Keep moving! Try to reach 12,000 steps today."
    )


st.divider()


# ==========================================================
# DAILY HEALTH REPORT
# ==========================================================

st.subheader(
    "📋 Daily Health Report"
)


col1, col2, col3 = st.columns(3)


with col1:

    if steps >= 10000:

        st.success(
            "✅ Activity Level\n\nExcellent"
        )

    else:

        st.warning(
            "⚠ Activity Level\n\nNeeds Improvement"
        )


with col2:

    if water >= 2.5:

        st.success(
            "💧 Hydration\n\nGood"
        )

    else:

        st.warning(
            "💧 Hydration\n\nDrink More Water"
        )


with col3:

    if sedentary <= 700:

        st.success(
            "🪑 Sedentary Time\n\nHealthy"
        )

    else:

        st.error(
            "🪑 Sedentary Time\n\nToo High"
        )


st.divider()


# ==========================================================
# HEALTH TIPS
# ==========================================================

st.subheader(
    "❤️ AI Health Tips"
)


tips = [

    "🚶 Walk for at least 30 minutes every day.",

    "💧 Drink 2.5–3 litres of water.",

    "🥗 Eat balanced meals rich in protein and fiber.",

    "😴 Sleep 7–8 hours every night.",

    "🏋 Include strength training at least twice a week.",

    "🧘 Stretch for 5–10 minutes after exercise."

]


for tip in tips:

    st.markdown(
        f"- {tip}"
    )


st.divider()


# ==========================================================
# PERFORMANCE DASHBOARD
# ==========================================================

st.subheader(
    "📊 Performance Dashboard"
)


# Normalize values to percentages

step_score = min(
    (steps / 10000) * 100,
    100
)

calorie_score = min(
    (calories / 2500) * 100,
    100
)

active_score = min(
    (active / 45) * 100,
    100
)

water_score = min(
    (water / 3) * 100,
    100
)

sedentary_score = max(
    0,
    100 - (sedentary / 12)
)


performance = {

    "Metric": [
        "Steps",
        "Calories",
        "Activity",
        "Hydration",
        "Low Sedentary"
    ],

    "Score": [
        step_score,
        calorie_score,
        active_score,
        water_score,
        sedentary_score
    ]

}


# IMPORTANT:
# fill="toself" is applied using update_traces()
# instead of passing it to px.line_polar()

fig = px.line_polar(

    performance,

    r="Score",

    theta="Metric",

    line_close=True,

    template="plotly_white"

)


fig.update_traces(
    fill="toself"
)


fig.update_layout(

    height=500,

    margin=dict(
        l=20,
        r=20,
        t=40,
        b=20
    )

)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# ==========================================================
# ACHIEVEMENT BADGES
# ==========================================================

st.subheader(
    "🏆 Achievement Badges"
)


c1, c2, c3, c4 = st.columns(4)


with c1:

    if steps >= 10000:

        st.success(
            "🥇\n\nStep Master"
        )

    else:

        st.info(
            "⬜\n\nStep Master"
        )


with c2:

    if water >= 2.5:

        st.success(
            "💧\n\nHydration Hero"
        )

    else:

        st.info(
            "⬜\n\nHydration Hero"
        )


with c3:

    if active >= 45:

        st.success(
            "💪\n\nWorkout Warrior"
        )

    else:

        st.info(
            "⬜\n\nWorkout Warrior"
        )


with c4:

    if score >= 90:

        st.success(
            "⭐\n\nFitness Champion"
        )

    else:

        st.info(
            "⬜\n\nFitness Champion"
        )


st.divider()


# ==========================================================
# PERFORMANCE LEVEL
# ==========================================================

st.subheader(
    "🎖 Performance Level"
)


if score >= 95:

    level = "🏆 Elite Athlete"

elif score >= 85:

    level = "🥇 Excellent"

elif score >= 70:

    level = "🥈 Active"

elif score >= 55:

    level = "🥉 Beginner"

else:

    level = "🔰 Getting Started"


st.metric(
    "Current Level",
    level
)


st.divider()


# ==========================================================
# DAILY TARGETS
# ==========================================================

st.subheader(
    "🎯 Daily Targets"
)


target1, target2 = st.columns(2)


with target1:

    st.progress(
        min(steps / 10000, 1.0)
    )

    st.write(
        f"Steps: {steps:,}/10,000"
    )


    st.progress(
        min(active / 45, 1.0)
    )

    st.write(
        f"Active Minutes: {active}/45"
    )


with target2:

    st.progress(
        min(water / 3.0, 1.0)
    )

    st.write(
        f"Water Intake: {water:.1f}/3 L"
    )


    st.progress(
        min(calories / 2500, 1.0)
    )

    st.write(
        f"Calories Burned: {calories}/2500"
    )


st.divider()


# ==========================================================
# DAILY MOTIVATION
# ==========================================================

quotes = [

    "🏃 Every step counts toward a healthier life.",

    "💪 Consistency beats intensity.",

    "🌱 Small improvements every day lead to big results.",

    "🔥 Stay active. Stay healthy.",

    "🚶 Your future self will thank you."

]


st.subheader(
    "🌟 Daily Motivation"
)


st.success(
    random.choice(quotes)
)


st.divider()


# ==========================================================
# WEEKLY FITNESS TREND
# ==========================================================

st.subheader(
    "📈 Weekly Fitness Trend"
)


week_data = pd.DataFrame({

    "Day": [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ],

    "Steps": [

        max(0, steps - 1800),

        max(0, steps - 1400),

        max(0, steps - 900),

        max(0, steps - 500),

        max(0, steps - 200),

        steps,

        min(15000, steps + 600)

    ]

})


fig = px.area(

    week_data,

    x="Day",

    y="Steps",

    markers=True,

    title="Weekly Step Progress",

    template="plotly_white"

)


fig.update_layout(
    height=350
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# ==========================================================
# AI HEALTH RISK
# ==========================================================

st.subheader(
    "🩺 AI Health Risk Assessment"
)


risk_score = 0


if sedentary > 900:

    risk_score += 35


if water < 2:

    risk_score += 20


if steps < 7000:

    risk_score += 25


if active < 20:

    risk_score += 20


risk_score = min(
    risk_score,
    100
)


if risk_score <= 25:

    st.success(
        "🟢 Low Health Risk"
    )

elif risk_score <= 50:

    st.warning(
        "🟡 Moderate Health Risk"
    )

else:

    st.error(
        "🔴 High Health Risk"
    )


st.progress(
    (100 - risk_score) / 100
)


st.write(
    f"Overall Wellness Score : **{100 - risk_score}/100**"
)


st.divider()


# ==========================================================
# DAILY NUTRITION
# ==========================================================

st.subheader(
    "🥗 AI Nutrition Suggestions"
)


if calories < 1800:

    st.info(
        """
🍎 Increase healthy calorie intake.

Suggested foods:

• Oats
• Eggs
• Banana
• Peanut Butter
• Milk
"""
    )

elif calories < 2500:

    st.success(
        """
🥗 Balanced Nutrition

Continue eating:

• Fruits
• Vegetables
• Lean Protein
• Whole Grains
"""
    )

else:

    st.warning(
        """
🔥 High Energy Expenditure

Ensure recovery with:

• Protein-rich meals
• Electrolytes
• Plenty of water
"""
    )


st.divider()


# ==========================================================
# SLEEP RECOMMENDATION
# ==========================================================

st.subheader(
    "😴 Sleep Recommendation"
)


recommended_sleep = 8


st.metric(
    "Recommended Sleep",
    f"{recommended_sleep} Hours"
)


if score > 90:

    st.success(
        "Excellent activity detected. Prioritize 8 hours of sleep for recovery."
    )

elif score > 70:

    st.info(
        "Aim for at least 7.5–8 hours of quality sleep."
    )

else:

    st.warning(
        "Proper sleep will help improve tomorrow's performance."
    )


st.divider()


# ==========================================================
# HEART HEALTH
# ==========================================================

st.subheader(
    "❤️ Heart Health Indicator"
)


heart = min(
    int(
        (active * 2 + steps / 200) / 2
    ),
    100
)


st.progress(
    heart / 100
)


if heart > 85:

    st.success(
        "Excellent Cardiovascular Activity"
    )

elif heart > 60:

    st.info(
        "Healthy Heart Activity"
    )

else:

    st.warning(
        "Increase aerobic activity"
    )


st.divider()


# ==========================================================
# AI SUMMARY
# ==========================================================

st.subheader(
    "🤖 Final AI Summary"
)


summary = []


if score >= 90:

    summary.append(
        "🏆 Outstanding fitness level."
    )

elif score >= 75:

    summary.append(
        "💪 Good overall fitness."
    )

else:

    summary.append(
        "🚶 Improve daily activity."
    )


if sedentary > 800:

    summary.append(
        "🪑 Reduce prolonged sitting."
    )


if water < 2.5:

    summary.append(
        "💧 Increase water intake."
    )


if active < 30:

    summary.append(
        "🏃 Exercise for another 15–20 minutes."
    )


if calories < 2200:

    summary.append(
        "🔥 Increase daily movement."
    )


for item in summary:

    st.success(item)


# ==========================================================
# FINAL DASHBOARD SUMMARY
# ==========================================================

st.divider()

st.subheader(
    "📌 Today's Overall Performance"
)


overall1, overall2, overall3 = st.columns(3)


with overall1:

    st.metric(
        "🏃 Activity Score",
        f"{step_score:.0f}%"
    )


with overall2:

    st.metric(
        "💪 Fitness Score",
        f"{score}/100"
    )


with overall3:

    st.metric(
        "❤️ Wellness Score",
        f"{100 - risk_score}/100"
    )


st.divider()


# ==========================================================
# QUICK HEALTH CHECKLIST
# ==========================================================

st.subheader(
    "✅ Daily Health Checklist"
)


checklist = {

    "10,000 Steps":
        steps >= 10000,

    "30 Active Minutes":
        active >= 30,

    "Drink 2.5L Water":
        water >= 2.5,

    "Sedentary Time < 700 min":
        sedentary <= 700,

    "Healthy Calorie Burn":
        calories >= 2200

}


for item, completed in checklist.items():

    if completed:

        st.success(
            f"✔ {item}"
        )

    else:

        st.error(
            f"✖ {item}"
        )


st.divider()


# ==========================================================
# AI MOTIVATION
# ==========================================================

st.subheader(
    "🌟 AI Motivation"
)


messages = {

    "excellent":
    """
🏆 Amazing work!

You're maintaining a healthy and active lifestyle.

Keep doing exactly what you're doing.
""",

    "good":
    """
💪 Good progress!

A little more walking and hydration will improve your score.
""",

    "average":
    """
🚶 Small improvements every day create big changes.

Stay consistent.
""",

    "poor":
    """
🔥 Today wasn't your best day.

Tomorrow is another opportunity.

Start with one healthy habit.
"""

}


if score >= 90:

    st.success(
        messages["excellent"]
    )

elif score >= 75:

    st.info(
        messages["good"]
    )

elif score >= 55:

    st.warning(
        messages["average"]
    )

else:

    st.error(
        messages["poor"]
    )


st.divider()


# ==========================================================
# AI COACH REPORT
# ==========================================================

st.subheader(
    "📄 AI Coach Report"
)


report = f"""
FITINTEL AI DAILY REPORT

Fitness Score : {score}/100

Today's Steps : {steps:,}

Calories Burned : {calories}

Water Intake : {water} L

Very Active Minutes : {active}

Sedentary Minutes : {sedentary}

Overall Wellness : {100 - risk_score}/100

AI Recommendation:

• Stay Active

• Drink Water

• Sleep 8 Hours

• Maintain Daily Exercise

Generated by FitIntel AI
"""


st.download_button(

    label="⬇ Download Today's Report",

    data=report,

    file_name="FitIntel_AI_Report.txt",

    mime="text/plain"

)


st.divider()


# ==========================================================
# ABOUT AI COACH
# ==========================================================

with st.expander(
    "ℹ About AI Coach"
):

    st.write(
        """
The AI Coach analyzes your fitness data and provides
personalized recommendations using intelligent rules.

Current Features

• Fitness Score
• Goal Analysis
• Calorie Analysis
• Hydration Monitoring
• Sedentary Detection
• Weekly Challenge
• Nutrition Advice
• Heart Health Indicator
• Sleep Recommendation
• Wellness Score

Future Scope

• Heart Rate Integration
• Fitbit API
• Google Fit
• Apple Health
• Wearable Device Support
• LLM-powered Personal Coach
"""
    )


st.divider()


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.markdown(
    """
    ### 💪 FitIntel AI

    **AI-Powered Fitness Analytics Platform**

    Developed by **Thejaswini S**  
    B.E Artificial Intelligence & Machine Learning

    `FastAPI` • `Streamlit` • `Machine Learning` • `Plotly` • `Python`

    **Version 1.0**

    © 2026 All Rights Reserved
    """
)