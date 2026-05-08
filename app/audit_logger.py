import json
from datetime import datetime


def save_email_log(data):

    try:

        with open(
            "outputs/generated_emails.json",
            "r"
        ) as file:

            logs = json.load(file)

    except:

        logs = []

    logs.append(data)

    with open(
        "outputs/generated_emails.json",
        "w"
    ) as file:

        json.dump(logs, file, indent=4)