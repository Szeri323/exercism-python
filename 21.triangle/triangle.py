def check_triangle(sides):
    if sides[0] > 0 and sides[1] > 0 and sides[2] > 0:
        if sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
            return True
    return False

def equilateral(sides):
    return check_triangle(sides) and (sides[0] == sides[1] and sides[1] == sides[2])


def isosceles(sides):
    if check_triangle(sides):
        if equilateral(sides):
            return True
        else:
            return ((sides[0] == sides[1] and sides[1] != sides[2]) or (sides[0] != sides[1] and sides[1] == sides[2]) or (sides[0] == sides[1] and sides[0] != sides[2]) or (sides[0] == sides[2] and sides[0] != sides[1]))
    return False
    return check_triangle(sides) and equilateral(sides) or ((sides[0] == sides[1] and sides[1] != sides[2]) or (sides[0] != sides[1] and sides[1] == sides[2]) or (sides[0] == sides[1] and sides[0] != sides[2]))


def scalene(sides):
    return check_triangle(sides) and not(equilateral(sides)) and not(isosceles(sides))
