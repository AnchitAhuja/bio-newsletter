"""
sender.py — Gmail SMTP delivery
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


def send_email(briefing: str, sender_email: str, sender_app_password: str,
               recipient_email: str, subject_template: str = "📊 Before It's Obvious — {date}") -> bool:

    date_str = datetime.now().strftime("%B %d, %Y")
    subject = subject_template.format(date=date_str)

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg.attach(MIMEText(briefing, "plain", "utf-8"))

    print(f"\n📧 Sending to {recipient_email}...")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_app_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("✓ Email sent")
        return True

    except smtplib.SMTPAuthenticationError:
        print("✗ Gmail auth failed — use App Password, not your Gmail password")
        print("  Get one at: myaccount.google.com/apppasswords")
        return False

    except Exception as e:
        print(f"✗ Send failed: {e}")
        return False
