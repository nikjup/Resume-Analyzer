
from google import genai
import os


def call_ai(resume_text, job_description, prompt):
    api_key = os.getenv("Gemini_key")
    if not api_key:
        return "simulation mode: AI not Connected"
    try:
        final_prompt = (
            prompt +
            "\n\nJob Description:\n" + job_description +
            "\n\nResume:\n" + resume_text
        )
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=final_prompt
            )
        return  response.text
    except Exception as e:
        return "billing not availaible"



