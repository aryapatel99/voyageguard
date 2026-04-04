from tools import get_weather, get_advisory
from risk_engine import calculate_risk
from database import save_trip_evaluation
from gemini_helper import generate_explanation


def evaluate_trip(destination, travel_date, budget, estimated_cost):

    # Step 1: Get data from tools
    weather = get_weather(destination)
    advisory = get_advisory(destination)

    # Step 2: Calculate risk
    risk_result = calculate_risk(weather, advisory, budget, estimated_cost)

    # Step 3: Generate AI explanation
    explanation = generate_explanation(
        destination,
        weather,
        advisory,
        risk_result["risk_level"]
    )

    # Step 4: Prepare data for DB
    data = {
        "destination": destination,
        "travel_date": travel_date,
        "budget": budget,
        "weather_risk": risk_result["weather_risk"],
        "advisory_risk": risk_result["advisory_risk"],
        "budget_risk": risk_result["budget_risk"],
        "final_score": risk_result["final_score"],
        "risk_level": risk_result["risk_level"],
        "explanation": explanation
    }

    # Step 5: Save to database
    save_trip_evaluation(data)

    # Step 6: Add explanation to output
    risk_result["explanation"] = explanation

    return risk_result


# Optional: only for testing
if __name__ == "__main__":
    result = evaluate_trip(
        destination="Mumbai",
        travel_date="2026-03-25",
        budget=30000,
        estimated_cost=35000
    )

    print(result)