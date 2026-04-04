def get_weather(destination):
    weather_data = {
        "mumbai": "heavy_rain",
        "delhi": "clear",
        "goa": "moderate"
    }

    # Default value for unknown cities
    return weather_data.get(destination.lower(), "moderate")


def get_advisory(destination):
    advisory_data = {
        "mumbai": "medium",
        "delhi": "low",
        "goa": "low"
    }

    # Default value for unknown cities
    return advisory_data.get(destination.lower(), "medium")