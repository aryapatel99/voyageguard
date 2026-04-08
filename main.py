import streamlit as st
from agent import evaluate_trip
from database import get_trip_history
import base64
import pandas as pd
import matplotlib.pyplot as plt


# ---------- BACKGROUND IMAGE ----------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{data}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("vg.jpg")


# ---------- TITLE ----------
st.title("🌍 VoyageGuard Dashboard")

st.write("Analyze travel risk using AI-powered insights")


# ---------- INPUT ----------
destination = st.text_input("Destination")
travel_date = st.text_input("Travel Date (YYYY-MM-DD)")
budget = st.number_input("Your Budget", min_value=0)
estimated_cost = st.number_input("Estimated Trip Cost", min_value=0)


# ---------- BUTTON ----------
if st.button("Evaluate Trip"):

    if destination.strip() == "":
        st.warning("Please enter a destination")

    else:
        result = evaluate_trip(
            destination,
            travel_date,
            budget,
            estimated_cost
        )

        st.markdown("---")

        # ---------- DASHBOARD CARDS ----------
        st.subheader("📊 Risk Dashboard")

        col1, col2, col3 = st.columns(3)

        col1.metric("🌧️ Weather", result["weather_risk"])
        col2.metric("⚠️ Advisory", result["advisory_risk"])
        col3.metric("💸 Budget", result["budget_risk"])

        st.markdown("---")

        # ---------- SCORE + CRITICAL ----------
        col1, col2 = st.columns(2)

        col1.metric("🎯 Final Score", f"{result['final_score']} / 100")
        col2.metric("🔥 Critical Factor", result["critical"])

        # ---------- RISK MESSAGE ----------
        if result["risk_level"] == "High":
            st.error("🚨 High Risk Trip - Not Recommended")
        elif result["risk_level"] == "Caution":
            st.warning("⚠️ Moderate Risk - Plan Carefully")
        else:
            st.success("✅ Safe Trip - Enjoy your journey")

        st.markdown("---")

        # ---------- AI EXPLANATION ----------
        st.subheader("🧠 AI Explanation")
        st.markdown(result["explanation"])

        st.markdown("---")

        # ---------- TABLE ----------
        st.subheader("📋 Risk Summary Table")

        st.table({
            "Factor": ["Weather 🌧️", "Advisory ⚠️", "Budget 💸"],
            "Score": [
                result["weather_risk"],
                result["advisory_risk"],
                result["budget_risk"]
            ],
            "Max": ["100", "100", "100"]
        })

        st.markdown("---")

        # ---------- CHART ----------
        st.subheader("📊 Risk Visualization")

        data = {
            "Weather": result["weather_risk"],
            "Advisory": result["advisory_risk"],
            "Budget": result["budget_risk"]
        }

        df = pd.DataFrame(list(data.items()), columns=["Factor", "Score"])

        fig, ax = plt.subplots()
        ax.bar(df["Factor"], df["Score"])
        ax.set_ylabel("Risk Score")
        ax.set_title("Risk Distribution")

        st.pyplot(fig)

        st.markdown("---")


# ---------- HISTORY ----------
st.subheader("📜 Previous Trip Evaluations")

history = get_trip_history()

if history:
    for trip in history:
        st.write(
            f"🌍 {trip['destination']} | 🎯 {trip['final_score']}/100 | 🚨 {trip['risk_level']}"
        )
else:
    st.write("No previous trips found.")