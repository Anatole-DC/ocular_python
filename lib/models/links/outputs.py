from typing import Tuple, List
from random import randint

class DiffusionMode:
    COPY: int = 0
    SPREAD: int = 1

class Output:
    def __init__(self, diffusion_mode: int = DiffusionMode.COPY):
        self._diffusion_mode: int = diffusion_mode
        self._links = []

        # Index for spread diffusion
        self._diffusion_index: int = 0

    def set_copy(self, value):
        [link.set(value) for link in self._links]

    #@TODO: Not working very well, seek for improvement...
    def set_spread(self, value):
        self._links[self._diffusion_index % len(self._links)].set(value)
        self._diffusion_index += 1

    def set(self, value):
        [self.set_copy, self.set_spread][self._diffusion_mode](value)

    def set_link(self, link):
        self._links.append(link)
        return self

    def is_linked(self):
        return self._links is not None


class FrameOutput(Output):
    ...
