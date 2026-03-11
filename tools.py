def get_weather(destination):
    weather_data = {
        "mumbai": "heavy_rain",
        "delhi": "clear",
        "goa": "moderate"
    }
    return weather_data.get(destination.lower(), "clear")


def get_advisory(destination):
    advisory_data = {
        "mumbai": "medium",
        "delhi": "low",
        "goa": "low"
    }
    return advisory_data.get(destination.lower(), "low")