def score(x, y):
    # define radii of circles
    INNER = 1
    MIDDLE = 5
    OUTER = 10

    # calculate distance from (x, y) to center (0, 0)
    # if it is less than the radius of a circle, (x, y) is inside that circle
    
    # if (x-center_x)**2 + (y-center_y)**2 <= radius**2:
    # inside circle

    # see https://stackoverflow.com/questions/481144/equation-for-testing-if-a-point-is-inside-a-circle
    # for further discussion

    line = x**2 + y**2

    if line <= INNER**2:
        return 10

    if line <= MIDDLE**2:
        return 5

    if line <= OUTER**2:
        return 1

    return 0