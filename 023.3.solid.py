"""
    Liskov Substitution principle: "Objects in program should be replaceable whit instances of their base types without
                                    altering the correctness of the program"
"""

import math


class Shape:

    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius


def calculate_area_and_perimeter(shapes):
    for shape in shapes:
        area = shape.get_area()
        perimeter = shape.get_perimeter()
        print(f"Area of {type(shape)}: {area}")
        print(f"Perimeter of {type(shape)}: {perimeter}")


shapes = [Shape(), Circle(2)]
calculate_area_and_perimeter(shapes)
