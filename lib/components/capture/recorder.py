import os
from typing import Tuple

import cv2 as opencv

from lib.models.frame import Frame
from lib.components.base_component import BaseComponent
from lib.models.links.inputs import Input


class RecorderComponent(BaseComponent):
    def __init__(self, path: str, video_name: str, resolution: Tuple[int, int] = (640, 480), fps: int = 25,  name: str = None):
        super().__init__(name=name)
        self._path: str = path
        self._video_name: str = video_name
        self._inputs["frames"] = Input()
        self._resolution: Tuple[int, int] = resolution
        self._fps: int = fps
        self._writer = opencv.VideoWriter(
            f"{self._path}/{self._video_name}.avi",
            opencv.VideoWriter_fourcc(*'XVID'),
            self._fps,
            self._resolution
        )

    def initiate(self):
        if not os.path.exists(self._path):
            os.mkdir(self._path)
            print(f">>> [{self._name}] WARNING : path didn't exist and was created ({self._path})")
    
    def do(self):
        frame: Frame = self._inputs["frames"].get()

        if frame is not None:
            new_frame = opencv.resize(frame.image, self._resolution)
            self._writer.write(new_frame)

    def terminate(self):
        self._writer.release()