import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def judge_reply(customer: str, generated: str, ideal: str) -> dict:
    prompt = f"""
    You are evaluating a customer support reply.
    Customer email: {customer}
    Generated reply: {generated}
    Ideal reply: {ideal}

    Rate the generated reply on:
    - Tone (polite, professional) [1-5]
    - Helpfulness (does it solve the problem) [1-5]
    - Completeness (covers all aspects of the query) [1-5]

    Return scores as JSON with keys tone, helpfulness, completeness.
    """
    model = genai.GenerativeModel("gemini-3-flash-preview")
    response = model.generate_content(prompt)
    try:
        import json
        scores = json.loads(response.text)
    except Exception:
        scores = {"tone": 3, "helpfulness": 3, "completeness": 3}
    return scores
