import pytest
from src.triangle import Triangle
# from src.figure import Figure

@pytest.mark.parametrize('side_a, side_b, side_c, perimeter, area',
                         [
                             (2,2,3,7,1.98),
                             (15.98, 89.98, 83.15, 189.11, 622.63),

                         ]
)
def test_triangle(side_a, side_b, side_c, perimeter, area):
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.name == 'Triangle'
    assert triangle.get_perimeter() == perimeter
    assert triangle.get_area() == area

@pytest.mark.parametrize('side_a, side_b, side_c',
                         [
                             (0,2,3),
                             (2,0,3),
                             (2, 2, 0),
                             (-1, 2, 3),
                             (2, -100, 3),
                             (2,0,-2147483648),
                         ])
def test_triangle_value_error(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        triangle = Triangle(side_a, side_b, side_c)

@pytest.mark.parametrize('side_a, side_b, side_c',
                         [
                             ('0',2,3),
                             (2,'0',3),
                             (2,2,'0'),
                             (None, 2, 3),
                             (2, None, 3),
                             (2, 2, None),
                             (True, 2, 3),
                             (2,True,3),
                             (2,2,True),
                             ([2,3,4],2,3),
                             (2,2,[2,3])
                         ])
def test_triangle_type_errors(side_a, side_b, side_c):
    with pytest.raises(TypeError):
        triangle = Triangle(side_a, side_b, side_c)

def test_triangle_add_area():
    triangle1 = Triangle(2,2,3)
    triangle2 = Triangle(15.98, 89.98, 83.15)
    assert triangle1.add_area(triangle2) == 624.61


