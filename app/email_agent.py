from groq import Groq

from config import GROQ_API_KEY
from prompts import build_email_prompt


client = Groq(api_key=GROQ_API_KEY)

def parse_email_response(email_text):

    subject = ""
    body = ""

    lines = email_text.split("\n")

    for i, line in enumerate(lines):

        if "subject" in line.lower():

            subject = line.replace(
                "**",
                ""
            ).replace(
                "Subject:",
                ""
            ).replace(
                "1. Subject:",
                ""
            ).strip()

            body = "\n".join(lines[i+1:]).strip()

            break

    return {
        "subject": subject,
        "body": body
    }

def generate_email(
    client_name,
    invoice_no,
    amount,
    overdue_days,
    tone
):

    prompt = build_email_prompt(
        client_name,
        invoice_no,
        amount,
        overdue_days,
        tone
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a professional finance collection assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4
    )

    email_text = response.choices[0].message.content

    parsed_email = parse_email_response(email_text)

    return parsed_email


