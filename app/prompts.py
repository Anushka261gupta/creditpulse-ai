def build_email_prompt(
    client_name,
    invoice_no,
    amount,
    overdue_days,
    tone
):

    return f"""
You are an AI Finance Collection Assistant for Travel Corporation India (TCI).

Generate a professional payment follow-up email.

Client Name: {client_name}
Invoice Number: {invoice_no}
Amount Due: ₹{amount}
Days Overdue: {overdue_days}
Tone: {tone}

Instructions:
- Maintain professionalism
- Adjust urgency according to tone
- Keep the email concise
- Mention invoice details clearly
- Do NOT use placeholders like:
  [Your Name]
  [Company Name]
  [Contact Information]
- Use:
  Finance Team
  Travel Corporation India (TCI)

Generate:
1. Subject
2. Email Body
"""