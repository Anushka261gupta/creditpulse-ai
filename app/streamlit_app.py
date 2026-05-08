import os
import streamlit as st

from app.utils import load_invoices
from app.escalation_engine import get_stage
from app.email_agent import generate_email
from app.audit_logger import save_email_log


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="CreditPulse AI",
    layout="wide"
)


# ---------------- HEADER ---------------- #

st.title("CreditPulse AI")

st.subheader("AI Finance Credit Follow-Up Agent")

st.caption(
    "Dry Run Mode Enabled — Emails are simulated and not actually sent."
)

st.markdown("""
This AI agent automatically:

- Detects overdue invoices
- Applies escalation logic
- Generates AI-powered follow-up emails
- Maintains audit logs
- Flags high-risk accounts for manual review
""")


# ---------------- LOAD CSV ---------------- #

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

csv_path = os.path.join(
    BASE_DIR,
    "data",
    "invoices.csv"
)

df = load_invoices(csv_path)


# ---------------- METRICS ---------------- #

total_invoices = len(df)

legal_cases = len(
    df[df["followup_count"] >= 4]
)

generated_cases = total_invoices - legal_cases

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Invoices",
    total_invoices
)

col2.metric(
    "Emails Generated",
    generated_cases
)

col3.metric(
    "Legal Escalations",
    legal_cases
)


# ---------------- MAIN LOOP ---------------- #

for _, row in df.iterrows():

    tone, overdue_days = get_stage(
        row["due_date"]
    )

    st.divider()

    st.write(
        f"### Client: {row['client_name']}"
    )

    st.write(
        f"Invoice: {row['invoice_no']}"
    )

    st.write(
        f"Amount: ₹{row['amount']}"
    )

    st.write(
        f"Days Overdue: {overdue_days}"
    )

    # Tone styling

    if tone == "Warm & Friendly":

        st.success(
            f"Tone: {tone}"
        )

    elif tone == "Polite but Firm":

        st.warning(
            f"Tone: {tone}"
        )

    elif tone == "Formal & Serious":

        st.error(
            f"Tone: {tone}"
        )

    else:

        st.error(
            f"Tone: {tone}"
        )


    # Legal escalation

    if tone == "Escalate to Legal":

        st.error(
            "FLAGGED FOR MANUAL REVIEW"
        )

        continue


    # Generate button

    if st.button(
        f"Generate Email for {row['invoice_no']}",
        key=row["invoice_no"]
    ):

        try:

            email = generate_email(
                row["client_name"],
                row["invoice_no"],
                row["amount"],
                overdue_days,
                tone
            )

            st.success(
                "Email Generated Successfully"
            )

            st.write("### Subject")

            st.write(
                email["subject"]
            )

            st.write("### Body")

            st.text_area(
                "Generated Email Body",
                email["body"],
                height=250
            )

            # Save audit log

            log_data = {

                "client":
                row["client_name"],

                "invoice":
                row["invoice_no"],

                "tone":
                tone,

                "days_overdue":
                overdue_days,

                "subject":
                email["subject"],

                "body":
                email["body"]
            }

            save_email_log(
                log_data
            )

        except Exception as e:

            st.error(
                f"Error generating email: {str(e)}"
            )