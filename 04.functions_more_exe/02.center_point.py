from math import floor


def coordinate_check(point_x1, point_y1, point_x2, point_y2):
    closes_x = None
    closes_y = None
    p1 = abs(point_x1) + abs(point_y1)
    p2 = abs(point_x2) + abs(point_y2)
    if p1 < p2:
        closes_x = point_x1
        closes_y = point_y1
    else:
        closes_x = point_x2
        closes_y = point_y2

    return f'({int(closes_x)}, {int(closes_y)})'


point_x1 = floor(float(input()))
point_y1 = floor(float(input()))
point_x2 = floor(float(input()))
point_y2 = floor(float(input()))
print(coordinate_check(point_x1, point_y1, point_x2, point_y2))
