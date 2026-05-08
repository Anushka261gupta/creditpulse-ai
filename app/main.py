from app.utils import load_invoices
from app.escalation_engine import get_stage
from app.email_agent import generate_email
from app.audit_logger import save_email_log

def main():

    df = load_invoices("data/invoices.csv")

    for _, row in df.iterrows():

        tone, overdue_days = get_stage(row["due_date"])

        print("\n============================")
        print("Client:", row["client_name"])
        print("Invoice:", row["invoice_no"])
        print("Tone:", tone)

        # Legal escalation case
        if tone == "Escalate to Legal":

            print("FLAGGED FOR MANUAL REVIEW")
            continue

        email = generate_email(
            row["client_name"],
            row["invoice_no"],
            row["amount"],
            overdue_days,
            tone
        )

        print("\nGenerated Email:\n")
        print("\nSubject:")
        print(email["subject"])

        print("\nBody:")
        print(email["body"])

        log_data = {
        "client": row["client_name"],
        "invoice": row["invoice_no"],
        "tone": tone,
        "days_overdue": overdue_days,
        "subject": email["subject"],
        "body": email["body"],
        }

        save_email_log(log_data)


if __name__ == "__main__":
    main()