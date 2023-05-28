from time import sleep
from datetime import datetime
from typing import Dict
import cv2 as opencv

from lib.models.frame import Frame
from lib.components.base_component import BaseComponent
from lib.models.links.inputs import FrameInput


class DisplayerComponent(BaseComponent):
    def __init__(self, name: str = "DisplayerComponent"):
        super().__init__(name=name)
        self._inputs = {
            "frames": FrameInput()
        }
    
    def initiate(self):
        super().initiate()
        opencv.namedWindow(self._name, opencv.WINDOW_NORMAL)

    def do(self):
        frame: Frame = self._inputs["frames"].get()

        if frame is not None:
            opencv.imshow(self._name, frame.image)

        if opencv.waitKey(30) == 27:
            self.pause()

    def terminate(self):
        super().terminate()
        opencv.destroyWindow(self._name)
