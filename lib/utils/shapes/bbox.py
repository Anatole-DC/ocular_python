import cv2 as opencv

from lib.helper.geometry import middle_point
from lib.utils.shapes.shapes import Point
from lib.utils.drawing.drawables import Drawables
from lib.utils.drawing.colors import Color

class BBox(Drawables):
    def __init__(self, pt1: Point, pt2: Point, color: Color = None) -> None:
        super().__init__(color)
        self._pt1 = pt1
        self._pt2 = pt2

    def draw(self, image, color: Color = None):
        opencv.rectangle(image, self._pt1.value(), self._pt2.value(), self._color.cv_color() if color is None else color.cv_color(), 2)

    def center(self) -> Point:
        return middle_point(self._pt1, self._pt2)

    @property
    def pt1(self):
        return self._pt1
    
    @property
    def pt2(self):
        return self._pt2

    def __str__(self) -> str:
        return f"({self._pt1.x}, {self._pt1.y}) ({self._pt2.x}, {self._pt2.y})"