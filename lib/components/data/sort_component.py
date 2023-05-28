from typing import Dict, List
from lib.components.base_component import BaseComponent
from lib.models.frame import Frame
from lib.models.links.link import BaseLink, FrameLink, ListLink

class FrameSorterComponent(BaseComponent):
    def __init__(self, name: str = "FrameSorterComponent"):
        super().__init__()
        self._inputs: Dict[str, ListLink] = {
            "frames": ListLink()
        }

        self._outputs: Dict[str, FrameLink] = {
            "frames": FrameLink()
        }

        self._current_index: int = 0
        self._FRAME_BUFFER: List[Frame] = []

    def do(self):
        frame = self._inputs["frames"].get()
        if frame is not None:
            self._FRAME_BUFFER.append(frame)

        if self._outputs["frames"].is_linked() and self._FRAME_BUFFER:
            for index, frame in enumerate(self._FRAME_BUFFER):
                if frame._index == self._current_index:
                    self._outputs["frames"].set(frame)
                    self._FRAME_BUFFER.pop(index)
                    self._current_index += 1
                    break
