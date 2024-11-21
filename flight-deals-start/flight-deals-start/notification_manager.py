import os
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv(".env.txt")

TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TWILIO_SID = os.getenv("ACCOUNT_SID")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
MY_CELL = os.getenv("MY_CELL")
# MY_EMAIL = os.getenv("MY_EMAIL")
# EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
# SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)
        self.my_email = os.getenv("MY_EMAIL")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.smtp_address = os.getenv("SMTP_ADDRESS")

    def send_message(self, message_body):
        message = self.client.messages.create(

            body= message_body,

            from_= TWILIO_NUMBER,

            to= MY_CELL,

        )
        print(message.status)

    def send_emails(self, email_list, body):
        for email in email_list:
            with smtplib.SMTP(self.smtp_address) as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.email_password)
                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=email,
                    msg="Subject:Cheap Flight Alert!\n\n"
                        f"{body}"
                )
