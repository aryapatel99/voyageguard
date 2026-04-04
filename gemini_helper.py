import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


def generate_explanation(destination, weather, advisory, risk_level):

    # Use stable working model
    model = genai.GenerativeModel("gemini-pro")

    prompt = prompt = f"""
You are a travel safety assistant.

Provide a clear, structured and user-friendly explanation.

Include:
1. Short summary
2. Reasons (bullet points)
3. Recommendation

Use simple language and include emojis.

Details:
Destination: {destination}
Weather: {weather}
Advisory: {advisory}
Risk Level: {risk_level}
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # fallback if API fails
        return f"Trip risk is {risk_level} due to {weather} weather and {advisory} advisory."