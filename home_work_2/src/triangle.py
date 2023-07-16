from src.figure import Figure


class Triangle(Figure):

    def __init__(self, side_a=2, side_b=2, side_c=3):
        # initialize base super class
        super().__init__()
        # checking if passed values are numbers
        if super().is_not_number(side_a) or super().is_not_number(side_b) or super().is_not_number(side_c):
            raise TypeError("Only numbers float or int are allowed")
        # checking if passed values greater then zero
        if side_a < 0 or side_b < 0 or side_c < 0:
            raise ValueError("At least one number was negative")
        # checking if passed values forms real triangle
        if self.can_triangle_exist(side_a, side_b, side_c):
            self.__side_a = side_a
            self.__side_b = side_b
            self.__side_c = side_c
            self.name = 'Triangle'
        else:
            raise ValueError("Passed values cannot format the triangle,\
                                at least one side greater then summ of two another")

    def can_triangle_exist(self, side_a, side_b, side_c):
        if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
            return True
        else:
            return False

    def test_function(self):
        print("some test function")

    def get_perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c

    def get_area(self):
        #a, b, c = self.__side_a, self.__side_b, self.__side_c
        semi_perimeter = self.get_perimeter() / 2
        return round((semi_perimeter * (semi_perimeter - self.__side_a) * (semi_perimeter - self.__side_b) * (semi_perimeter - self.__side_c)) ** 0.5, 2)

    def __str__(self):
        return f'{self.name} has sides: {self.__side_a}, {self.__side_b}, {self.__side_c}\
        , area: {self.get_area()}\
        , perimeter: {self.get_perimeter()}'

