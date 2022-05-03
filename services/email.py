import os
import smtplib
from email.message import EmailMessage


def send_email(sender, receiver, subject, body):
    """
    Send an email from a given sender to a given receiver.
    """

    EMAIL_STMP_SERVICE = os.getenv('EMAIL_STMP_SERVICE')
    EMAIL_SMTP_PORT = os.getenv('EMAIL_SMTP_PORT')
    server = smtplib.SMTP(EMAIL_STMP_SERVICE, EMAIL_SMTP_PORT)

    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    server.starttls()
    server.login(sender, EMAIL_PASSWORD)

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(body)

    server.send_message(msg)
