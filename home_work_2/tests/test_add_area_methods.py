import pytest
from src.rectangle import Rectangle
from src.triangle import Triangle
from src.square import Square
from src.circle import Circle


def test_add_area_mix_types():
    rectangle = Rectangle(2,6)
    triangle = Triangle(2,2,3)
    square = Square(4)
    circle = Circle(2)
    assert rectangle.add_area(triangle) == 13.98
    assert triangle.add_area(square) == 17.98
    assert square.add_area(circle) == 28.5664
    assert circle.add_area(rectangle) == 24.5664

def test_add_area_value_error():
    rectangle = Rectangle(2, 6)
    triangle = Triangle(2, 2, 3)
    square = Square(4)
    circle = Circle(2)
    with pytest.raises(ValueError):
        rectangle.add_area(5)
        triangle.add_area('123')
        square.add_area(True)
        circle.add_area([1,2,3])

