from typing import Dict

from lib.components.base_component import BaseComponent
from lib.models.frame import Frame
from lib.models.links.inputs import FrameInput
from lib.models.links.outputs import FrameOutput

class BaseProcessingComponent(BaseComponent):
    def __init__(self, name: str = "BaseProcessingComponent"):
        super().__init__(name)
        self._inputs: Dict[str, FrameInput] = {
            "frames": FrameInput()
        }
        self._outputs: Dict[str, FrameOutput] = {
            "frames": FrameOutput()
        }