from dataclasses import dataclass, asdict
from typing import override, Self
from abc import ABC, abstractmethod
import math

@dataclass
class Form(ABC):
    name: str

    @abstractmethod
    def translate(self, deltaX: float, deltaY: float) -> None:
        pass

    @classmethod
    def copy(cls, f: Self) -> Self:
        # print(asdict(f))
        # print(cls)
        return cls(**asdict(f))

@dataclass
class Point(Form):
    x: float
    y: float

    @override
    def translate(self, deltaX: float, deltaY: float) -> None:
        self.x += deltaX
        self.y += deltaY

    def distance(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)
    

@dataclass
class WeightedPoint(Point):
    weight: float

    @override
    def distance(self, other: Point) -> float:
        # TODO: compute a real distance with weights (1 if normal point)
        return self.weight * super().distance(other)
    
    @staticmethod
    def from_point_weight(point: Point, weight: float) -> "WeightedPoint":
        """construct a new WeightedPoint from a Point and an external weight
        """
        return WeightedPoint(name=point.name, x=point.x, y=point.y, weight=weight)

@dataclass
class ColoredPoint(Point):
    color: str


@dataclass
class WeightedColoredPoint(WeightedPoint, ColoredPoint):
    pass
