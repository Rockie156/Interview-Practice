def get_distance(p1, p2):
    x1 = p1[0]
    x2 = p2[0]

    y1 = p1[1]
    y2 = p2[1]
    x_squared_dist = (x1 - x2) ** 2
    y_squared_dist = (y1 - y2) ** 2

    sum_squared_dist = x_squared_dist + y_squared_dist

    return sum_squared_dist ** .5
