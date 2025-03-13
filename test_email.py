import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load credentials from environment variables
load_dotenv("config.env")

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
RECIPIENT_EMAIL = "beezy592742@gmail.com"  # Change if needed

def send_test_email():
    """Sends a simple test email to verify SMTP login."""
    if not EMAIL_USER or not EMAIL_PASS:
        print("⚠️ Email credentials are missing. Check your config.env file.")
        return

    msg = MIMEText("This is a test email from the SCADA alert system.")
    msg["Subject"] = "SCADA Test Email"
    msg["From"] = EMAIL_USER
    msg["To"] = RECIPIENT_EMAIL

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(msg["From"], msg["To"], msg.as_string())
        print("Test email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    send_test_email()