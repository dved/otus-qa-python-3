import pytest
from src.rectangle import Rectangle

@pytest.mark.parametrize('side_a, side_b, perimeter, area',
                         [
                             (2, 6, 16, 12),
                             (2.5, 3.16, 11.32, 7.9)
                         ])
def test_rectangle(side_a, side_b, perimeter, area):
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.name == 'Rectangle'
    assert rectangle.get_perimeter() == perimeter
    assert rectangle.get_area() == area

@pytest.mark.parametrize('side_a, side_b',
                         [
                             (-1,8),
                             (4,0),
                             (345, -2147483648)
                         ])
def test_rectangle_value_errors(side_a, side_b):
    with pytest.raises(ValueError):
        rectangle = Rectangle(side_a, side_b)

@pytest.mark.parametrize('side_a, side_b',
                         [
                             (None,8),
                             (4,'0'),
                             (True,89.98)
                         ])
def test_rectangle_type_errors(side_a, side_b):
    with pytest.raises(TypeError):
        rectangle = Rectangle(side_a, side_b)
