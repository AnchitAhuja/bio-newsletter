"""
sender.py — SendGrid email delivery
"""

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime


def send_email(briefing: str, sender_email: str, sender_app_password: str,
               recipient_email: str, subject_template: str = "📊 Before It's Obvious — {date}") -> bool:

    date_str = datetime.now().strftime("%B %d, %Y")
    subject = subject_template.format(date=date_str)

    message = Mail(
        from_email=sender_email,
        to_emails=recipient_email,
        subject=subject,
        plain_text_content=briefing
    )

    print(f"\n📧 Sending to {recipient_email}...")

    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(f"✓ Email sent (status {response.status_code})")
        return True

    except Exception as e:
        print(f"✗ Send failed: {e}")
        return False
