from datetime import datetime

def get_stage(due_date):

    due = datetime.strptime(due_date, "%Y-%m-%d")
    today = datetime.today()

    overdue_days = (today - due).days

    if overdue_days <= 7:
        return "Warm & Friendly", overdue_days

    elif overdue_days <= 14:
        return "Polite but Firm", overdue_days

    elif overdue_days <= 21:
        return "Formal & Serious", overdue_days

    elif overdue_days <= 30:
        return "Stern & Urgent", overdue_days

    else:
        return "Escalate to Legal", overdue_days