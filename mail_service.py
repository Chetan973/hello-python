import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

class MailService:
    def __init__(self):
        self.sender_email = os.getenv("SENDER_EMAIL")
        self.sender_password = os.getenv("SENDER_PASSWORD")
        self.smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", 587))

    def send_email(self, receiver_email, subject, body):
        if not self.sender_email or not self.sender_password:
            raise ValueError("Sender email and password must be set in environment variables.")

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.sender_email
        msg["To"] = receiver_email

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            print(f"Email sent successfully to {receiver_email}")
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

if __name__ == "__main__":
    # Example usage (requires .env file with SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL)
    mail_service = MailService()
    receiver = os.getenv("RECEIVER_EMAIL")
    if receiver:
        mail_service.send_email(receiver, "Test Subject", "This is a test email from the Python mail service.")
    else:
        print("RECEIVER_EMAIL not set in .env, skipping example.")
