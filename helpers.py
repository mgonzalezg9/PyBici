from math import pi, cos, asin, sqrt

from constants import BIKE_NUM_ATTRIBUTE


def fixed_point_distance(first: dict, second: dict) -> int:
    """
        Calculates the distance between two fixed points defined by latitude and longitude.
    """
    p = pi/180
    a = 0.5 - cos((second['latitude']-first['latitude'])*p)/2 + cos(first['latitude']*p) * \
        cos(second['latitude']*p) * \
        (1-cos((second['longitude']-first['longitude'])*p))/2
    return 12742 * asin(sqrt(a))


def get_closest_stops(stops: list, ref_point: dict) -> list:
    """
        Returns the stops ordered by distance to a reference point.
    """

    # Filtering stops with bikes...
    stops_with_bikes = [stop for stop in stops if int(
        stop[BIKE_NUM_ATTRIBUTE]) > 0]

    # Ordering by distance to a fixed point...
    stops_ordered = sorted(
        stops_with_bikes, key=lambda stop: fixed_point_distance(stop, ref_point))

    return stops_ordered
