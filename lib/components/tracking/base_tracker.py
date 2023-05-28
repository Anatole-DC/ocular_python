from typing import Dict, List
from time import sleep

from lib.components.base_component import BaseComponent
from lib.models.trajectory import Trajectory
from lib.utils.shapes.bbox import BBox
from lib.models.links.inputs import Input
from lib.models.links.outputs import Output

class BaseTrackeComponent(BaseComponent):
    def __init__(self, name: str = None):
        super().__init__(name=name)
        self._TRAJECTORIES_BUFFER: List[Trajectory] = []
        self._inputs: Dict[str, Input] = {
            "detections": Input()
        }
        self._outputs: Dict[str, Output] = {
            "trajectories": Output(),
            "lost_trajectories": Output(),
        }

    def track(self, detection: BBox) -> List[Trajectory]:
        ...
    
    def do(self):
        detections: List[BBox] = self._inputs["detections"].get()

        if detections is not None:
            for detection in detections:
                self._TRAJECTORIES_BUFFER = self.track(detection)

            if self._outputs["trajectories"].is_linked():
                self.outputs["trajectories"].set(self._TRAJECTORIES_BUFFER)

            if self._outputs["lost_trajectories"].is_linked():
                self.outputs["lost_trajectories"].set(
                    [trajectory for trajectory in self._TRAJECTORIES_BUFFER if trajectory.is_lost()]
                )

            [self._TRAJECTORIES_BUFFER.pop(index) for index, trajectory in enumerate(self._TRAJECTORIES_BUFFER) if trajectory.is_lost()]
