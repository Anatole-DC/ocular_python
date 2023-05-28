from typing import Dict

from lib.components.base_component import BaseComponent
from lib.models.links.inputs import Input, FrameInput
from lib.models.links.outputs import Output, FrameOutput
from lib.models.frame import Frame


class BaseDetectorComponent(BaseComponent):
    def __init__(self, name: str = "DetectorComponent"):
        super().__init__(name=name)

        self._inputs: Dict[str, Input] = {
            "frames": FrameInput()
        }
        self._outputs: Dict[str, Output] = {
            "frames": FrameOutput(),
            "detections": Output()
        }