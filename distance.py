from math import sqrt


def distance(p1=(0, 0), p2=(1, 1)):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
