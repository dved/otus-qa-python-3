import numbers
from typing import Any
from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, other_figure):
        if isinstance(other_figure, Figure):
            return self.get_area() + other_figure.get_area()
        else:
            raise ValueError(f"Expected instance of the class Figure, got {other_figure}")

    def is_not_number(self, variable: Any):
        # type(variable) better than isinstance
        # If we pass bool then isinstance will return True, because bool is subclass of int
        if type(variable) not in (int, float):
            return True
        else:
            return False
