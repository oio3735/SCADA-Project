import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load credentials from environment variables (Set these before running)
load_dotenv("config.env")
EMAIL_USER = os.getenv("EMAIL_USER")  # Sender's email
EMAIL_PASS = os.getenv("EMAIL_PASS")  # App password (not your real password)
RECIPIENT_EMAIL = "booyewunmi@gmail.com"  # Alert recipient

def send_alert(sensor, value):
    """Sends an email alert when a sensor value exceeds the threshold."""
    if not EMAIL_USER or not EMAIL_PASS:
        print("Email credentials are missing. Set EMAIL_USER and EMAIL_PASS.")
        return

    msg = MIMEText(f"🚨 ALERT! {sensor} exceeded limit: {value}")
    msg["Subject"] = "Diamondback SCADA Alert"
    msg["From"] = EMAIL_USER
    msg["To"] = RECIPIENT_EMAIL

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(msg["From"], msg["To"], msg.as_string())
        print(f"Alert sent: {sensor} exceeded {value}")
    except Exception as e:
        print(f"Error sending email: {e}")

# Test email sending when this script is run directly
if __name__ == "__main__":
    send_alert("Test Sensor", 999)