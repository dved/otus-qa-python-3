from src.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side_a):
        # initialize base super class
        super().__init__(side_a, side_a)
        # all checks for numbers or if the the number is positive should be done during initializing super Rectangle class
        self.side_a = side_a
        self.name = 'Square'

    def get_perimeter(self):
        return super().get_perimeter()

    def get_area(self):
        return super().get_area()

    def __str__(self):
        return f'{self.name} has side: {self.side_a}\
        , area: {self.get_area()}\
        , perimeter: {self.get_perimeter()}'


