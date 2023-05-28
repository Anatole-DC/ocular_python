from typing import List

import cv2 as opencv

from lib.components.detection.base_detector import BaseDetectorComponent
from lib.models.frame import Frame
from lib.utils.shapes.bbox import BBox
from lib.utils.shapes.shapes import Point


class HaarCascadeDetectorComponent(BaseDetectorComponent):
    def __init__(self, detector_path: str, name: str = "HaarCascadeDetectorComponent"):
        super().__init__(name=name)
        self._detector_path: str = detector_path
        self.body_classifier = opencv.CascadeClassifier(self._detector_path)

    def do(self):
        frame: Frame = self.inputs["frames"].get()

        if frame is not None:
            bboxes: List[BBox] = [
                BBox(
                    Point(detection[0], detection[1]),
                    Point(detection[0] + detection[2], detection[1] + detection[3])
                )
                for detection in self.body_classifier.detectMultiScale(
                    frame.image,
                    scaleFactor=1.05,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags=opencv.CASCADE_SCALE_IMAGE
                )
            ]

            frame.set_elements(bboxes)

            if self._outputs["frames"].is_linked():
                self._outputs["frames"].set(frame)

            if self._outputs["detections"].is_linked():
                self._outputs["detections"].set(bboxes)