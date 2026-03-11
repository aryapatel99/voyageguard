def calculate_risk(weather_condition,advisory_level,user_budget,estimated_cost):
    
    #weather scoring
    weather_scores={
        "storm":40,
        "heavy_rain":30,
        "moderate":15,
        "clear":5
    }
    
    weather_risk = weather_scores.get(weather_condition.lower(), 10)

    # Advisory scoring
    advisory_scores = {
        "high": 40,
        "medium": 20,
        "low": 5
    }
    advisory_risk = advisory_scores.get(advisory_level.lower(), 10)

    # Budget scoring
    if user_budget < estimated_cost:
        budget_risk = 25
    else:
        budget_risk = 5

    # Final risk calculation
    final_score = weather_risk + advisory_risk + budget_risk

    if final_score >= 75:
        risk_level = "High"
    elif final_score >= 40:
        risk_level = "Caution"
    else:
        risk_level = "Low"          

    return {
        "weather_risk": weather_risk,           
        "advisory_risk": advisory_risk,
        "budget_risk": budget_risk,
        "final_score": final_score,
        "risk_level": risk_level
    }
    