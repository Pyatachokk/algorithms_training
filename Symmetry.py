
points = [(1, 1), (2, 1), (2, 3), (2, 2), (3, 1), (4, 1)]


def check_sym(points):
    if len(points) == 0 or len(points) == 1:
        return True

    points.sort()
    right = points[len(points) // 2:]
    right.sort(key=lambda k: (k[0], -k[1]))
    points[len(points) // 2:] = right
    axis = (points[0][0] + points[-1][0]) / 2

    i = 0
    j = len(points) - 1
    while i != j and i - j != 1:
        if (points[i][1] == points[j][1] and points[i][0] - axis == -(points[j][0] - axis)) or\
                points[i][0] == points[j][0] == axis:
            i += 1
            j -= 1
        else:
            return False
    if i == j and points[i][0] != axis:
        return False
    else:
        return True


print(check_sym(points))