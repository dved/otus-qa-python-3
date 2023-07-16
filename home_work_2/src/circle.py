from src.figure import Figure
from math import pi

class Circle(Figure):
    def __init__(self, radius):
        # initialize base super class
        super().__init__()
        # checking if passed values are numbers
        if super().is_not_number(radius):
            raise TypeError("Only numbers float or int are allowed")
        # checking if passed values greater then zero
        if radius <= 0:
            raise ValueError("Radius should be greater then 0")
        self.radius = radius
        self.name = 'Circle'

    def get_perimeter(self):
        return round((2 * pi * self.radius), 4)


    def get_area(self):
        return round(pi * (self.radius ** 2), 4)