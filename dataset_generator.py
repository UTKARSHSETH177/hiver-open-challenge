import json

def create_dataset():
    examples = [
        ("I can't access my invoice. Can you resend it?",
         "Thanks for reaching out. I've resent the invoice to your registered email. Please let us know if you face any further issues."),
        ("Do you offer discounts for nonprofits?",
         "We do offer special pricing for nonprofits. Could you share more details about your organization so we can assist you better?"),
        ("My account was charged twice. Please help.",
         "Sorry for the inconvenience. We've checked and refunded the duplicate charge. It should reflect in your account within 3-5 business days."),
        ("Can I upgrade my plan mid-cycle?",
         "Yes, you can upgrade anytime. The new plan will be applied immediately and charges will be adjusted on a pro-rata basis.")
    ]
    dataset = [{"customer": q, "ideal_reply": a} for q, a in examples]
    with open("data/sample_emails.json", "w") as f:
        json.dump(dataset, f, indent=2)

if __name__ == "__main__":
    create_dataset()
