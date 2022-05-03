import os
from dotenv import load_dotenv

from services.email import send_email
load_dotenv()

EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

send_email(EMAIL_SENDER, 'test@test.com',
           'MuyBici: Your near stops', 'Have a good ride!')
