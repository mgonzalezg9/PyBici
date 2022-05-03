import os
from requests import get
from dotenv import load_dotenv
from constants import BASE_URL, EMAIL_SUBJECT, FILTERS, BIKE_NUM_ATTRIBUTE, STOP_NAME_ATTRIBUTE
from services.email import send_email
from services.muy_bici import get_closest_stops

load_dotenv()

LATITUDE_COORD = os.getenv('LATITUDE_COORD')
LONGITUDE_COORD = os.getenv('LONGITUDE_COORD')

print('Requesting bike stops within its occupation...')
res = get(BASE_URL, params=FILTERS)
# Request fails
assert res.status_code == 200, f'Request failed. MuyBici server responsed with code {res.status_code} ☹️'

print('Obtained response. Now calculating the closest stops...')
near_stops = get_closest_stops(
    res.json()['data'], {'latitude': float(LATITUDE_COORD), 'longitude': float(LONGITUDE_COORD)})

msg = """
The closest three stops with bikes are:

********************************************************

%s
********************************************************

Have a good ride!
"""

bike_info = ""
for stop in near_stops[:3]:
    bike_info += f'\t{stop[STOP_NAME_ATTRIBUTE]}: {stop[BIKE_NUM_ATTRIBUTE]} bikes 🚲\n'

print(msg % bike_info)

EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
print(f'Sending email from {EMAIL_SENDER} to {EMAIL_RECEIVER}...')
send_email(EMAIL_SENDER, EMAIL_RECEIVER, EMAIL_SUBJECT, msg % bike_info)
