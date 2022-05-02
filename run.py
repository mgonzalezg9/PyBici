import os
from requests import get
from dotenv import load_dotenv
from constants import BASE_URL, FILTERS, BIKE_NUM_ATTRIBUTE, STOP_NAME_ATTRIBUTE
from helpers import get_closest_stops

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

print()
print('The closest three stops with bikes are:')
print('********************************************************')
for stop in near_stops[:3]:
    print(
        f'\t{stop[STOP_NAME_ATTRIBUTE]}: {stop[BIKE_NUM_ATTRIBUTE]} bikes 🚲')
print('********************************************************')
print('Have a good ride!')
