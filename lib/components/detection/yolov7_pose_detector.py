from typing import List

import cv2 as opencv
import numpy as np
import torch

from lib.components.detection.base_detector import BaseDetectorComponent
from lib.models.frame import Frame
from lib.utils.shapes.bbox import BBox
from lib.utils.shapes.shapes import Point
from lib.models.links.outputs import Output



class YoloV7PoseDetectorComponent(BaseDetectorComponent):
    def __init__(self, model_path: str, name: str = "YoloV7DetectorComponent"):
        super().__init__(name=name)
        self._model_path: str = model_path
        self._model = torch.hub.load('/home/anatole/Projets/ocular/lab/yolov7/', 'custom', self._model_path, source='local')
        self._outputs["frames"] = Output()

    def do(self):
        frame: Frame = self._inputs["frames"].get()

        if frame is not None:
            image = [frame.image]
            predictions = self._model(image)

            # results: List = predictions.xyxy[0].tolist()

            # detections: List[BBox] = [
            #     BBox(
            #         Point(int(x1), int(y1)), Point(int(x2), int(y2))
            #     )
            #     for x1, y1, x2, y2, _, _ in results
            # ]

            if self._outputs["frames"].is_linked():
                self._outputs["frames"].set(frame)
