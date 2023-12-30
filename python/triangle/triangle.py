def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    sides_exist = a > 0 and b > 0 and c > 0
    all_sides_equal = (a == b and b == c)
    return sides_exist and all_sides_equal


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    sides_exist = a > 0 and b > 0 and c > 0
    two_sides_equal = (a == b or (b == c or a == c))
    triangle_inequality = 2 * max(a, b, c) < a + b + c
    return sides_exist and triangle_inequality and two_sides_equal


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    sides_exist = a > 0 and b > 0 and c > 0
    sides_different = a != b and b != c and a != c
    triangle_inequality = 2 * max(a, b, c) < a + b + c
    return sides_exist and triangle_inequality and sides_different
