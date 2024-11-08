def check_triangle(sides: list) -> bool:
    if 0 in sides or sum(sides) < 2*(max(sides)):
        return False
    return True


def equilateral(sides: list) -> bool:
    return check_triangle(sides) and (sides[0] == sides[1] and sides[1] == sides[2])


def isosceles(sides: list) -> bool:
    sorted_sides = sorted(sides)
    if equilateral(sides) or check_triangle(sides) and not(equilateral(sides)) and (sorted_sides[0] == sorted_sides[1] or sorted_sides[1] == sorted_sides[2]):
        return True
    return False


def scalene(sides: list) -> bool:
    return check_triangle(sides) and not(equilateral(sides)) and not(isosceles(sides))
