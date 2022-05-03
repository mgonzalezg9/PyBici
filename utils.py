from math import pi, cos, asin, sqrt


def fixed_point_distance(first: dict, second: dict) -> int:
    """
        Calculates the distance between two fixed points defined by latitude and longitude.
    """
    p = pi/180
    a = 0.5 - cos((second['latitude']-first['latitude'])*p)/2 + cos(first['latitude']*p) * \
        cos(second['latitude']*p) * \
        (1-cos((second['longitude']-first['longitude'])*p))/2
    return 12742 * asin(sqrt(a))
