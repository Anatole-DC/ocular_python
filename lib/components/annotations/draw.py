from time import sleep
from typing import Dict, Generator, List
from lib.utils.drawing.drawables import Drawables
from lib.components.base_component import BaseComponent
from lib.models.frame import Frame
from lib.models.links.inputs import Input, FrameInput
from lib.models.links.outputs import Output, FrameOutput
from lib.utils.shapes.bbox import BBox
from lib.utils.shapes.shapes import Point

import cv2 as opencv


class DrawComponent(BaseComponent):
    def __init__(self, name: str = "DrawComponent"):
        super().__init__(name=name)
        self._inputs: Dict[str, Input] = {
            "frames": FrameInput(),
            "elements": Input()
        }
        self._outputs: Dict[str, Output] = {
            "frames": FrameOutput()
        }

    def do(self):
        frame: Frame = self._inputs["frames"].get()
        elements: List[Drawables] = self._inputs["elements"].get()

        if frame is not None:
            frame.set_elements(elements)
            frame.draw()
            if self._outputs["frames"].is_linked():
                self._outputs["frames"].set(frame)
        else:
            sleep(0.1)
