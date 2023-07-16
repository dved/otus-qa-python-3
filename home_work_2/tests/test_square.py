import pytest
from src.square import Square

@pytest.mark.parametrize('side_a, perimeter, area',
                         [
                             (2, 8, 4),
                             (1.39, 5.56, 1.9321),
                         ])
def test_square(side_a, perimeter, area):
    square = Square(side_a)
    assert square.name == 'Square'
    assert square.get_perimeter() == perimeter
    assert square.get_area() == area

@pytest.mark.parametrize('side_a',
                         [-1,
                          0,
                          -2147483648,
                          -0.0001])
def test_square_value_errors(side_a):
    with pytest.raises(ValueError):
        square = Square(side_a)

@pytest.mark.parametrize('side_a',
                         ['9',
                          'a',
                          True,
                          None,
                          (2,3,4)])
def test_square_type_error(side_a):
    with pytest.raises(TypeError):
        square = Square(side_a)
        
def test_square_add_area():
    square1 = Square(2)
    square2 = Square(15.98)
    assert square1.add_area(square2) == 259.3604


