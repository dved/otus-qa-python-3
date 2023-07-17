from src.figure import Figure

class Rectangle(Figure):
    def __init__(self, side_a=1, side_b=1):
        # initialize base super class
        super().__init__()
        # checking if passed values are numbers
        if super().is_not_number(side_a) or super().is_not_number(side_b):
            raise TypeError("Only numbers float or int are allowed")
        # checking if passed values greater then zero
        if side_a <= 0 or side_b <= 0:
            raise ValueError("At least one number was negative")
        self.side_a = side_a
        self.side_b = side_b
        self.name = 'Rectangle'

    def get_perimeter(self):
        return round((self.side_a + self.side_b) * 2, 4)

    def get_area(self):
        return round(self.side_a * self.side_b, 4)

    def __str__(self):
        return f'{self.name} has sides: {self.side_a}, {self.side_b}\
        , area: {self.get_area()}\
        , perimeter: {self.get_perimeter()}'