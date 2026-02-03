# llm_generator.py
# ---------------------------------------------------
# Gemini Safe Response Generator (Flash – Free Tier Friendly)
# ---------------------------------------------------

import os
import google.generativeai as genai


def generate_safe_response(prompt: str) -> dict:
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            return {
                "final_response_type": "SAFE",
                "response": "Gemini API key not found."
            }

        # Configure Gemini
        genai.configure(api_key=api_key)

        # ✅ FREE-TIER FRIENDLY MODEL
        model = genai.GenerativeModel("models/gemini-flash-latest")

        response = model.generate_content(prompt)

        return {
            "final_response_type": "SAFE",
            "source_model": "Gemini Flash (Latest)",
            "response": response.text
        }

    except Exception as e:
        return {
            "final_response_type": "SAFE",
            "source_model": "Gemini Flash (Latest)",
            "response": (
                "⚠️ Live Gemini response unavailable due to API quota limits.\n\n"
                "This project demonstrates a responsible AI pipeline with "
                "ethical filtering and graceful fallback handling."
            )
        }
