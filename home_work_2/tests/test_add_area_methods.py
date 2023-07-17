import pytest
from src.rectangle import Rectangle
from src.triangle import Triangle
from src.square import Square
from src.circle import Circle


@pytest.mark.parametrize('test_figure, other_figure, area_sum',
                         [
                            (Rectangle(10, 12.57), Rectangle(0.5,39.897), 145.6485),
                            (Square(2), Square(15.98), 259.3604),
                            (Circle(2), Circle(15.98), 814.8048),
                            (Triangle(2,2,3), Triangle(15.98, 89.98, 83.15), 624.61),
                            (Rectangle(2,6), Triangle(2, 2, 3), 13.98),
                            (Triangle(2, 2, 3), Square(4), 17.98),
                            (Square(4), Circle(2), 28.5664),
                            (Circle(2), Rectangle(2,6), 24.5664)
                        ])
def test_add_area_mix_types(test_figure, other_figure, area_sum):
    assert test_figure.add_area(other_figure) == area_sum


@pytest.mark.parametrize('test_figure, area',
                         [
                             (Rectangle(2, 6), 5),
                             (Triangle(2, 2, 3), '123'),
                             (Square(4), True),
                             (Circle(2), [1,2,3])
                         ])
def test_add_area_value_error(test_figure, area):
    with pytest.raises(ValueError):
        test_figure.add_area(area)
