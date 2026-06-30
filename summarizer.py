import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv(
        "GOOGLE_API_KEY"
    )
)

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)

def generate_summary(text):

    prompt = f"""
    Summarize the following research paper.

    Include:
    1. Objective
    2. Methodology
    3. Results
    4. Conclusion

    Paper:
    {text[:10000]}
    """

    response = model.generate_content(
        prompt
    )

    return response.text