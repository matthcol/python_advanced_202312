from dataclasses import dataclass
from typing import override
import math

@dataclass
class Form:
    name: str


@dataclass
class Point(Form):
    x: float
    y: float

    def distance(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)
    

@dataclass
class WeightedPoint(Point):
    weight: float

    @override
    def distance(self, other: Point) -> float:
        # TODO: compute a real distance with weights (1 if normal point)
        return self.weight * super().distance(other)

@dataclass
class ColoredPoint(Point):
    color: str


@dataclass
class WeightedColoredPoint(WeightedPoint, ColoredPoint):
    pass
