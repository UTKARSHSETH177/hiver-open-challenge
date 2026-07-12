import google.generativeai as genai
import os

# Configure with your Google AI API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_reply(customer_email: str) -> str:
    prompt = f"""
    You are a customer support agent at Hiver.
    Here are examples of good replies:
    Customer: I can't access my invoice.
    Reply: Thanks for reaching out. I've resent the invoice to your registered email. Please let us know if you face any further issues.

    Customer: Do you offer discounts for nonprofits?
    Reply: We do offer special pricing for nonprofits. Could you share more details about your organization so we can assist you better?

    Now write a reply for:
    Customer: {customer_email}
    """
    model = genai.GenerativeModel("models/gemini-3-flash-preview")
    response = model.generate_content(prompt)
    return response.text.strip()
