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

    # Input validation
    if destination.strip() == "":
        st.warning("Please enter a destination")

    else:
        result = evaluate_trip(
            destination,
            travel_date,
            budget,
            estimated_cost
        )

        # Handle invalid destination error
        if "error" in result:
            st.error(result["error"])

        else:
            st.subheader("Risk Evaluation Result")

            st.write("Final Score:", result["final_score"])
            st.write("Risk Level:", result["risk_level"])

            st.write("Weather Risk:", result["weather_risk"])
            st.write("Advisory Risk:", result["advisory_risk"])
            st.write("Budget Risk:", result["budget_risk"])