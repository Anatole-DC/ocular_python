from typing import List

import torch

from lib.components.detection.base_detector import BaseDetectorComponent
from lib.models.frame import Frame
from lib.utils.shapes.bbox import BBox
from lib.utils.shapes.shapes import Point


class YoloV5DetectorComponent(BaseDetectorComponent):
    def __init__(self, model_path: str, name: str = "YoloV5DetectorComponent"):
        super().__init__(name=name)
        self._model_path: str = model_path
        self._model = torch.hub.load('/home/anatole/Projets/ocular/lab/yolov5/', 'custom', path=self._model_path, source='local')

    def do(self):
        frame: Frame = self._inputs["frames"].get()

        if frame is not None:
            image = [frame.image]
            predictions = self._model(image)

            results: List = predictions.xyxy[0].tolist()

            detections: List[BBox] = [
                BBox(
                    Point(int(x1), int(y1)), Point(int(x2), int(y2))
                )
                for x1, y1, x2, y2, _, _ in results
            ]

            if self._outputs["detections"].is_linked():
                self._outputs["detections"].set(detections)
