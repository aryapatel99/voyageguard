import streamlit as st
from agent import evaluate_trip

st.title("VoyageGuard - Travel Risk Evaluator")

st.write("Enter your trip details below:")

# User Inputs
destination = st.text_input("Destination")
travel_date = st.text_input("Travel Date (YYYY-MM-DD)")
budget = st.number_input("Your Budget", min_value=0)
estimated_cost = st.number_input("Estimated Trip Cost", min_value=0)

# Button
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

        # 🌍 Heading
        st.subheader("🌍 Trip Risk Analysis")

        # 📊 Breakdown
        st.markdown("### 📊 Risk Breakdown")

        st.write(f"Weather Risk: {result['weather_risk']} 🌧️")
        st.write(f"Advisory Risk: {result['advisory_risk']} ⚠️")
        st.write(f"Budget Risk: {result['budget_risk']} 💸")

        st.markdown("---")

        # 🎯 Score
        st.markdown(f"### 🎯 Final Score: {result['final_score']}")

        # 🚨 Risk Level with color
        if result["risk_level"] == "High":
            st.error(f"🚨 Risk Level: {result['risk_level']}")
        elif result["risk_level"] == "Medium":
            st.warning(f"⚠️ Risk Level: {result['risk_level']}")
        else:
            st.success(f"✅ Risk Level: {result['risk_level']}")

        st.markdown("---")

        # 🧠 AI Explanation
        st.markdown("### 🧠 AI Explanation")
        st.write(result["explanation"])