from datetime import datetime
from typing import Dict
import cv2 as opencv

from lib.components.base_component import BaseComponent
from lib.models.frame import Frame
from lib.models.links.outputs import FrameOutput, Output


class BaseCaptureComponent(BaseComponent):
    def __init__(self, channel, scale: float = 1.0, execution_mode: int = 0, name: str = "CameraComponent"):
        super().__init__(execution_mode=execution_mode, name=name)
        self._channel = channel
        self._scale: float = scale
        self._camera: opencv.VideoCapture = opencv.VideoCapture(self._channel)
        self._index: int = 0
        self._outputs = {
            "frames": Output()
        }

    def initiate(self):
        return super().initiate()

    def do(self):
        super().do()
        result, image = self._camera.read()
        if result:
            final_frame = opencv.resize(
                image,
                (
                    int(image.shape[1] * self._scale),
                    int(image.shape[0] * self._scale),
                ),
                interpolation=opencv.INTER_AREA
            )
            opencv.putText(final_frame, str(self._index), (10, 10), opencv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
            
            if self._outputs["frames"].is_linked():
                self._outputs["frames"].set(Frame(final_frame, self._index))

            self._index += 1

    def terminate(self):
        print(f"{self._name} was ended")
        self._camera.release()

    def get(self):
        while True:
            try:
                yield self._outputs["frames"]
            except KeyError:
                yield None
