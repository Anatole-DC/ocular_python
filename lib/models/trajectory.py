from datetime import datetime, timedelta
from typing import List

import cv2 as opencv

from lib.utils.drawing.drawables import Drawables
from lib.utils.shapes.shapes import Point
from lib.utils.shapes.bbox import BBox
from lib.utils.drawing.colors import Color, Colors


TIME_TO_TRAJECTORY_LOSS = timedelta(seconds=2)

class Trajectory(Drawables):
    def __init__(self) -> None:
        self._points: List[Point] = []
        self._last_update: datetime = datetime.now()
        self._last_bbox: BBox = None

    def is_lost(self) -> bool:
        return datetime.now() - self._last_update >  TIME_TO_TRAJECTORY_LOSS
    
    def update(self, bbox: BBox):
        self._points.append(bbox.center())
        self._last_bbox = bbox
        self._last_update = datetime.now()
        return self
    
    def draw(self, image, color: Color = Colors.RED) -> Color:
        self._last_bbox.draw(image, color)
        [
            opencv.line(image, pt1.value(), pt2.value(), self._color.cv_color() if color is None else color.cv_color(), 1)
            for pt1, pt2 in zip(self._points, self._points[1:])
        ]

    def direction(self) -> int:
        return int(self.points[-1].y < self.points[0].y)

    @property
    def points(self):
        return self._points

    @property
    def bbox(self):
        return self._last_bbox