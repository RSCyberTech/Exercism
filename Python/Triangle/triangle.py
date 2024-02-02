def equilateral(sides):
    if not testIfTriangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if not testIfTriangle(sides):
        return False
    return (sides[0] == sides[1]) or (sides[1] == sides[2]) or (sides[2] == sides[0])


def scalene(sides):
    if not testIfTriangle(sides):
        return False
    return sides[0] != sides[1] != sides[2] != sides[0]


def testIfTriangle(sides):
    for s in sides:
        if s <= 0:
            return False
        if s > (sum(sides) - s):
            return False
    return True
