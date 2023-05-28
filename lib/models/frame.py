from datetime import datetime
from typing import Dict, List

import cv2 as opencv
from numpy import ndarray


class Frame:
    def __init__(self, image, index, timestamp = None, elements = []):
        self._image: ndarray = image
        self._timestamp = datetime.now() if timestamp is None else timestamp
        self._elements: List = elements
        self._index: int = index

    def set_elements(self, elements):
        if elements is not None:
            elements = elements if isinstance(elements, List) else [elements]
            self._elements = self._elements + elements
        return self

    def draw(self):
        [element.draw(self._image) for element in self._elements]

    @property
    def image(self):
        return self._image


class FrameTest:
    def __init__(self, index: int, capture, timestamp = None, elements = None) -> None:
        self._index = index
        self._timestamp = datetime.now() if timestamp is None else timestamp
        self._elements = elements
        self._capture: opencv.VideoCapture = capture

    def image(self):
        # get total number of frames
        totalFrames = self._capture.get(opencv.CAP_PROP_FRAME_COUNT)

        # check for valid frame number
        if self._index >= 0 & self._index <= totalFrames:
            # set frame position
            opencv.set(opencv.CAP_PROP_POS_FRAMES, self._index)