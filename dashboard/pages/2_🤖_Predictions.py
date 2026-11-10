import streamlit as st
import requests

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Prediction Center",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# LOAD CSS
# --------------------------------------------------

def load_css():
    try:
        with open("dashboard/assets/style.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except:
        pass

load_css()

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class='main-title'>
🤖 AI Prediction Center
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='sub-title'>
Predict Goal Achievement and Calories Burned using Machine Learning
</div>
""", unsafe_allow_html=True)

st.write("")

st.info("Enter your activity details below and let the AI models predict your fitness performance.")

st.divider()

# --------------------------------------------------
# TABS
# --------------------------------------------------

goal_tab, calorie_tab = st.tabs([
    "🎯 Goal Prediction",
    "🔥 Calorie Prediction"
])

# ==================================================
# GOAL PREDICTION
# ==================================================

with goal_tab:

    st.subheader("🎯 Goal Achievement Prediction")

    left, right = st.columns(2)

    with left:

        total_distance = st.slider(
            "🏃 Total Distance (km)",
            0.0,
            25.0,
            5.5,
            0.1
        )

        very_active = st.slider(
            "💪 Very Active Minutes",
            0,
            180,
            30
        )

        fairly_active = st.slider(
            "🚶 Fairly Active Minutes",
            0,
            180,
            15
        )

    with right:

        lightly_active = st.slider(
            "🙂 Lightly Active Minutes",
            0,
            500,
            200
        )

        sedentary = st.slider(
            "🪑 Sedentary Minutes",
            0,
            1440,
            700
        )

        calories = st.slider(
            "🔥 Calories",
            1000,
            5000,
            2200
        )

    st.write("")

    if st.button(
        "🎯 Predict Goal Achievement",
        use_container_width=True
    ):

        payload = {

            "TotalDistance": total_distance,
            "VeryActiveMinutes": very_active,
            "FairlyActiveMinutes": fairly_active,
            "LightlyActiveMinutes": lightly_active,
            "SedentaryMinutes": sedentary,
            "Calories": calories

        }

        with st.spinner("AI is analyzing your fitness..."):

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/predict_goal",
                    json=payload,
                    timeout=10
                )

                response.raise_for_status()

                result = response.json()

                st.divider()

                if result["Goal Achieved"]:

                    st.success("✅ Congratulations! AI predicts you will achieve your daily goal.")

                    st.balloons()

                    st.markdown("""
### 🤖 AI Recommendation

Keep maintaining your activity level.

✔ Continue your workouts

✔ Stay hydrated

✔ Maintain consistent daily steps
""")

                else:

                    st.error("❌ AI predicts the daily goal may not be achieved.")

                    st.markdown("""
### 🤖 AI Recommendation

• Increase daily walking

• Reduce sedentary time

• Add 20–30 minutes of moderate exercise

• Aim for at least 10,000 steps
""")

            except Exception as e:

                st.error("⚠ Unable to connect to the FastAPI server.")
                st.code(str(e))
# ==================================================
# CALORIE PREDICTION
# ==================================================

with calorie_tab:

    st.subheader("🔥 Calorie Burn Prediction")

    left, right = st.columns(2)

    with left:

        steps = st.slider(
            "👣 Total Steps",
            0,
            30000,
            9000
        )

        distance = st.slider(
            "🏃 Total Distance (km)",
            0.0,
            25.0,
            6.0,
            0.1
        )

        very_active2 = st.slider(
            "💪 Very Active Minutes",
            0,
            180,
            30,
            key="va2"
        )

    with right:

        fairly_active2 = st.slider(
            "🚶 Fairly Active Minutes",
            0,
            180,
            20,
            key="fa2"
        )

        lightly_active2 = st.slider(
            "🙂 Lightly Active Minutes",
            0,
            500,
            220,
            key="la2"
        )

        sedentary2 = st.slider(
            "🪑 Sedentary Minutes",
            0,
            1440,
            700,
            key="sed2"
        )

    st.write("")

    if st.button(
        "🔥 Predict Calories Burned",
        use_container_width=True
    ):

        payload = {

            "TotalSteps": steps,
            "TotalDistance": distance,
            "VeryActiveMinutes": very_active2,
            "FairlyActiveMinutes": fairly_active2,
            "LightlyActiveMinutes": lightly_active2,
            "SedentaryMinutes": sedentary2

        }

        with st.spinner("Predicting Calories..."):

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/predict_calories",
                    json=payload,
                    timeout=10
                )

                response.raise_for_status()

                result = response.json()

                predicted = result["Predicted Calories"]

                st.divider()

                c1, c2 = st.columns(2)

                with c1:

                    st.metric(
                        "🔥 Predicted Calories",
                        f"{predicted:.0f} kcal"
                    )

                with c2:

                    if predicted >= 2800:

                        st.success("Excellent activity level")

                    elif predicted >= 2200:

                        st.info("Healthy calorie burn")

                    else:

                        st.warning("Try increasing daily activity")

                st.subheader("🤖 AI Recommendation")

                if predicted < 2000:

                    st.warning("""
• Walk more throughout the day

• Add 30 minutes of exercise

• Reduce sedentary time

• Aim for 10,000+ daily steps
""")

                elif predicted < 2800:

                    st.success("""
Great progress!

Maintain your current routine.

Add strength training 2–3 days/week.
""")

                else:

                    st.success("""
Excellent!

Your activity level is impressive.

Keep following your routine while ensuring proper recovery and hydration.
""")

            except Exception as e:

                st.error("⚠ FastAPI server is not running.")

                st.code(str(e))
st.divider()

st.markdown(
"""
### 💡 About AI Predictions

This page uses trained Machine Learning models to estimate:

- 🎯 Goal Achievement
- 🔥 Calories Burned

Models:
- Random Forest Classifier
- Random Forest Regressor

Backend:
- FastAPI REST API

Frontend:
- Streamlit
"""
)

st.caption(
    "FitIntel AI • Version 1.0 • Developed by Thejaswini S"
)