import pytest
from src.circle import Circle
# from src.figure import Figure

@pytest.mark.parametrize('radius, perimeter, area',
                         [
                             (2,12.5664,12.5664),
                             (15.98, 100.4053, 802.2384),
                             (0.01,0.0628,0.0003),
                             (0.001, 0.0063, 0),
                             (2147483647,13493037698.2388,1.4488038902661208e+19)
                         ])

def test_circle_positive_tests(radius, perimeter, area):
    circle = Circle(radius)
    assert circle.name == 'Circle'
    assert circle.get_perimeter() == perimeter
    assert circle.get_area() == area

@pytest.mark.parametrize('radius',
                         [-1,
                          0,
                          -2147483648,
                          -0.0001])
def test_circle_value_errors(radius):
    with pytest.raises(ValueError):
        circle = Circle(radius)

@pytest.mark.parametrize('radius',
                         ['9',
                          'a',
                          True,
                          None,
                          (2,3,4)])
def test_circle_type_error(radius):
    with pytest.raises(TypeError):
        circle = Circle(radius)
