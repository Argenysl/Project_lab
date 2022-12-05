from math import pi as p


def circle(radius):
    return 2 * radius * p


def rectangle(width, height):
    return width + height + width + height


def square(side):
    return side * 4


def triangle(side_1, side_2, side_3):
    return side_1 + side_2 + side_3
