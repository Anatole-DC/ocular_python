from typing import Any

from lib.models.frame import Frame


class Input:
    def __init__(self, input_type: type = None) -> None:
        self._input_type: type = input_type
        self._link = None

    def is_linked(self):
        return self._link is not None

    def set_link(self, link):
        self._link = link
        return self

    def get(self):
        if self.is_linked():
            return self._link.get()
        return None


class FrameInput(Input):
    def __init__(self, input_type: type = Frame) -> None:
        super().__init__(input_type)