def get_weather(destination):
    weather_data = {
        "mumbai": "heavy_rain",
        "delhi": "clear",
        "goa": "moderate"
    }

    if destination.lower() not in weather_data:
        return None

    return weather_data[destination.lower()]


def get_advisory(destination):
    advisory_data = {
        "mumbai": "medium",
        "delhi": "low",
        "goa": "low"
    }

    if destination.lower() not in advisory_data:
        return None

    return advisory_data[destination.lower()]