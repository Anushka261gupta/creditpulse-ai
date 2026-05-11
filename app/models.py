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

    return EmailResponse(
        subject=subject,
        body=body
    )
