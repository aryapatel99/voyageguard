import requests
from config import WEATHER_API_KEY


def get_weather(destination):
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": destination,
            "appid": WEATHER_API_KEY,
            "units": "metric"
        }

        response = requests.get(url, params=params)
        data = response.json()

        print("API RESPONSE:", data)

        if data.get("cod") != 200:
            return "moderate"

        weather_main = data["weather"][0]["main"].lower()

        if "rain" in weather_main:
            return "heavy_rain"
        elif "storm" in weather_main:
            return "storm"
        elif "cloud" in weather_main:
            return "moderate"
        else:
            return "clear"

    except Exception as e:
        print("ERROR:", e)
        return "moderate"


# 🔥 ADD THIS BACK
def get_advisory(destination):
    advisory_data = {
        "mumbai": "medium",
        "delhi": "low",
        "goa": "low"
    }

    return advisory_data.get(destination.lower(), "medium")