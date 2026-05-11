import sqlite3
from datetime import datetime


DB_NAME = "logs/audit.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS email_logs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            client TEXT,

            invoice TEXT,

            tone TEXT,

            days_overdue INTEGER,

            subject TEXT,

            body TEXT,

            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_email_log(log_data):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO email_logs (
            client,
            invoice,
            tone,
            days_overdue,
            subject,
            body,
            timestamp
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (

        log_data["client"],
        log_data["invoice"],
        log_data["tone"],
        log_data["days_overdue"],
        log_data["subject"],
        log_data["body"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def fetch_logs():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM email_logs
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows