from typing import Generator, List, Dict

import openpifpaf
from numba import jit, cuda, njit
import numpy as np

from lib.components.detection.base_detector import BaseDetectorComponent
from lib.models.pose import Pose
from lib.utils.shapes.shapes import Point
from lib.models.frame import Frame
from lib.models.links.outputs import Output


class PoseDetectorComponent(BaseDetectorComponent):
    def __init__(self, name: str = "PoseDetectorComponent"):
        super().__init__(name=name)
        self._detector = openpifpaf.Predictor(checkpoint="shufflenetv2k16")
        self._outputs["poses"] = Output()

    def predict(self, frame: np.ndarray) -> List:
        return self._detector.numpy_image(frame)

    def do(self):
        frame: Frame = self._inputs["frames"].get()

        if frame is not None:

            predictions, _, _ = self.predict(frame.image)

            poses: List[Pose] = []

            for prediction in predictions:
                poses.append(Pose(*[Point(int(keypoint[0]), int(keypoint[1])) for keypoint in prediction.data.tolist()]))

            output = frame.set_elements([pose for pose in poses])

            if self._outputs["frames"].is_linked():
                self._outputs["frames"].set(output)

            if self._outputs["detections"].is_linked():
                self._outputs["detections"].set([pose.bounding_box() for pose in poses])

            if self._outputs["poses"].is_linked():
                self._outputs["poses"].set(poses)