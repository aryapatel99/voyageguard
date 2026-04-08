import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


def generate_explanation(destination, weather, advisory, risk_level, critical, score):

    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
You are a travel safety expert.

STRICT RULES:
- 3 bullet points ONLY
- Each point must have emoji
- 40–50 words total
- Mention score out of 100
- Mention most critical factor
- If risk is LOW → do NOT warn

FORMAT:

• 🌦️ Weather: {weather}  
• ⚠️ Advisory: {advisory}  
• 💸 Budget impact  

🔥 Most Critical Factor: {critical}

👉 Recommendation: Clear advice

DATA:
Destination: {destination}
Score: {score}/100
Risk Level: {risk_level}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except:
        return f"""
• 🌦️ Weather is {weather}, affecting travel conditions  
• ⚠️ Advisory level is {advisory}, indicating situation  
• 💸 Budget influences overall trip comfort  

🔥 Most Critical Factor: {critical}

👉 Recommendation: {'Safe to travel' if risk_level == 'Low' else 'Travel with caution'}
"""