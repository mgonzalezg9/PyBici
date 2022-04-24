from requests import get
from constants import BASE_URL, FILTERS, BIKE_NUM_ATTRIBUTE, STOP_NAME_ATTRIBUTE
from env import REF_POINT
from helpers import fixed_point_distance

print('Requesting bike stops within its occupation...')
res = get(BASE_URL, params=FILTERS)

if res.status_code != 200:
    print(
        f'Request failed. MuyBici server responsed with code {res.status_code} ☹️')
    exit(1)

print('Filtering stops with bikes...')
stops = res.json()['data']
stops_with_bikes = [stop for stop in stops if int(
    stop[BIKE_NUM_ATTRIBUTE]) > 0]

print('Ordering by distance to a fixed point...')
stops_ordered = sorted(stops_with_bikes,
                       key=lambda stop: fixed_point_distance(
                           stop,
                           REF_POINT
                       ))

print()
print('The closest three stops with bikes are:')
print('********************************************************')
for stop in stops_ordered[:3]:
    print(f'\t{stop[STOP_NAME_ATTRIBUTE]}: {stop[BIKE_NUM_ATTRIBUTE]} bikes 🚲')
print('********************************************************')
