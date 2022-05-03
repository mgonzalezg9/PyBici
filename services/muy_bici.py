from constants import BIKE_NUM_ATTRIBUTE, MAX_ALLOWED_BIKES
from utils import fixed_point_distance


def get_closest_stops(stops: list, ref_point: dict) -> list:
    """
        Returns the stops ordered by distance to a reference point.
    """

    # Filtering stops with a reasonable amount of bikes
    stops_with_bikes = [stop for stop in stops if int(
        stop[BIKE_NUM_ATTRIBUTE]) > 0 and int(stop[BIKE_NUM_ATTRIBUTE]) < MAX_ALLOWED_BIKES]

    # Ordering by distance to a fixed point...
    stops_ordered = sorted(
        stops_with_bikes, key=lambda stop: fixed_point_distance(stop, ref_point))

    return stops_ordered
