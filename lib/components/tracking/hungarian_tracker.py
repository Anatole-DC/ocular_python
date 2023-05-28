from typing import List, Generator

from lib.components.tracking.base_tracker import BaseTrackeComponent
from lib.helper.tracking import get_iou
from lib.utils.shapes.bbox import BBox
from lib.models.trajectory import Trajectory


MIN_REQUIRED_IOU: float = 0.2

class HungarianTrackerComponent(BaseTrackeComponent):
    def __init__(self, name: str = "HungarianTrackerComponent"):
        super().__init__(name=name)


    def track(self, bbox: BBox) -> List[Trajectory]:
        # Buffer value
        max_value_index: int = 0
        max_ious: int = 0.0

        # Check if trajectories where already registered
        if self._TRAJECTORIES_BUFFER:
            ious: List[float] = [get_iou(bbox, trajectory.bbox) for trajectory in self._TRAJECTORIES_BUFFER]
            max_ious = max(ious)
            max_value_index: int = ious.index(max_ious)


        # Check if a result is above mix required_value
        if max_ious > MIN_REQUIRED_IOU:
            self._TRAJECTORIES_BUFFER[max_value_index].update(bbox)
            return self._TRAJECTORIES_BUFFER

        self._TRAJECTORIES_BUFFER.append(Trajectory().update(bbox))

        return self._TRAJECTORIES_BUFFER