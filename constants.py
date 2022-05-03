BASE_URL = 'https://muybici.es/api-labici.php'
FILTERS = {
    'module': 'parking',
    'method': 'get-locations',
    'city': 'MU'
}
BIKE_NUM_ATTRIBUTE = 'xocupados'
STOP_NAME_ATTRIBUTE = 'descripcion'
MAX_ALLOWED_BIKES = 4  # Stops with more than X bikes are suspicious to be not working

EMAIL_SUBJECT = 'MuyBici: Your near stops'
