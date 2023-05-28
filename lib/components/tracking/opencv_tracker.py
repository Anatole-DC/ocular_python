from typing import List

import cv2 as opencv

from lib.components.base_component import BaseComponent


class OpenCVTrackerComponent(BaseComponent):
    def __init__(self, name: str = "OpenCVTrackerComponent"):
        super().__init__(name=name)
        self._trackers: List = []
