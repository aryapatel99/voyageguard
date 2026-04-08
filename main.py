import streamlit as st
from agent import evaluate_trip
from database import get_trip_history
import base64


# ---------- BACKGROUND IMAGE ----------
##def set_bg(image_file):
##    with open(image_file, "rb") as f:
##        data = base64.b64encode(f.read()).decode()

##    st.markdown(
##        f"""
##        <style>
##        .stApp {{
##            background-image: url("data:image/jpg;base64,{data}");
##            background-size: cover;
##        }}
##        </style>
##        """,
##        unsafe_allow_html=True
##    )

# 👇 put your image name here
##set_bg("bg.jpg")


# ---------- TITLE ----------
st.title("🌍 VoyageGuard - Travel Risk Evaluator")

st.write("Enter your trip details below:")


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

        # ---------- OUTPUT ----------
        st.subheader("🌍 Trip Risk Analysis")

        st.markdown("### 📊 Risk Breakdown")

        st.write(f"Weather Risk: {result['weather_risk']} 🌧️")
        st.write(f"Advisory Risk: {result['advisory_risk']} ⚠️")
        st.write(f"Budget Risk: {result['budget_risk']} 💸")

        st.markdown("---")

        # 🎯 Score
        st.markdown(f"### 🎯 Final Score: {result['final_score']} / 100")

        # 🔥 Critical factor
        st.markdown(f"### 🔥 Most Critical Factor: {result['critical']}")

        # 🚨 Risk Level (FIXED LOGIC)
        if result["risk_level"] == "High":
            st.error("🚨 High Risk - Travel Not Recommended")
        elif result["risk_level"] == "Caution":
            st.warning("⚠️ Moderate Risk - Travel Carefully")
        else:
            st.success("✅ Safe to Travel")

        st.markdown("---")

        # 🧠 AI Explanation
        st.markdown("### 🧠 AI Explanation")
        st.markdown(result["explanation"])

        # 📊 TABLE
        st.markdown("### 📊 Risk Summary Table")

        st.table({
            "Factor": ["Weather 🌧️", "Advisory ⚠️", "Budget 💸"],
            "Score (out of 100)": [
                result["weather_risk"],
                result["advisory_risk"],
                result["budget_risk"]
            ]
        })

        st.markdown("---")


# ---------- HISTORY (FIXED POSITION) ----------
st.subheader("📜 Previous Trip Evaluations")

history = get_trip_history()

if history:
    for trip in history:
        st.write(
            f"🌍 {trip['destination']} | 🎯 {trip['final_score']}/100 | 🚨 {trip['risk_level']}"
        )
else:
    st.write("No previous trips found.")