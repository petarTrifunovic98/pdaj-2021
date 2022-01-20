import math


def calculate_distance(coord_pair1, coord_pair2):
    x1, y1 = coord_pair1
    x2, y2 = coord_pair2
    distance =  math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    return distance