from os import path
from time import sleep
from typing import List, Tuple

import cv2 as opencv

from lib.components.capture.base_capture_component import BaseCaptureComponent


class VideoComponent(BaseCaptureComponent):
    def __init__(self, channel: str, frame_interval: Tuple[int, int] = (0, None), execution_mode: int = 1, scale: float = 1.0, fps: int = 25, name: str = "VideoComponent"):
        super().__init__(channel=channel, scale=scale, execution_mode=execution_mode, name=name)
        self._fps: int = fps
        self._frame_interval: Tuple[int, int] = frame_interval

    def initiate(self):
        # super().initiate()
        # if not path.exists(self._channel):
        #     print(f"ERROR >>> File path does not exist : {self._channel}")
        #     self.stop()
        begin, _ = self._frame_interval

        # print(begin)
        if begin is not None:
            self._camera.set(1, begin)
            self._index = begin

    def do(self):
        super().do()
        if self._frame_interval[1] is not None and self._index == self._frame_interval[1]:
            print(f"We've reached the {self._frame_interval[1]} milestones")
            self.stop()
