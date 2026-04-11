from tools import get_weather, get_advisory
from risk_engine import calculate_risk
from database import save_trip_evaluation
from gemini_helper import generate_explanation


# Convert system weather → human readable
def interpret_weather(weather):
    if weather == "heavy_rain":
        return "rainy 🌧️"
    elif weather == "moderate":
        return "cloudy ⛅"
    elif weather == "clear":
        return "clear and sunny ☀️"
    else:
        return "normal weather"


def evaluate_trip(destination, travel_date, budget, estimated_cost):

    weather = get_weather(destination)
    advisory = get_advisory(destination)

    risk_result = calculate_risk(weather, advisory, budget, estimated_cost)

    # 👇 Human readable weather
    weather_text = interpret_weather(weather)

    # 👇 Find most critical factor
    risks = {
        "Weather": risk_result["weather_risk"],
        "Advisory": risk_result["advisory_risk"],
        "Budget": risk_result["budget_risk"]
    }
    critical = max(risks, key=risks.get)

    # 👇 AI Explanation
    explanation = generate_explanation(
        destination,
        weather_text,
        advisory,
        risk_result["risk_level"],
        critical,
        risk_result["final_score"]
    )

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

    # 🔥 SAFE DATABASE SAVE (VERY IMPORTANT FOR DEPLOYMENT)
    try:
        save_trip_evaluation(data)
    except Exception as e:
        print("Database not available:", e)

    risk_result["explanation"] = explanation
    risk_result["critical"] = critical

    return risk_result