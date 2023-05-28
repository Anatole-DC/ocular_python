from typing import List

from lib.components.base_component import BaseComponent
from lib.models.links.inputs import Input
from lib.models.links.outputs import Output
from lib.utils.shapes.shapes import Line
from lib.models.trajectory import Trajectory
from lib.helper.trajectories import intersects

class CrossingDirection:
    UP: int = 0
    DOWN: int = 1


class LineCrossingComponent(BaseComponent):
    def __init__(self, line: Line, name: str = "TrajectoryAnalysisComponent"):
        super().__init__(name=name)
        self._inputs["trajectories"] = Input()
        self._outputs["counting"] = Output()
        self._outputs["line"] = Output()
        self._line: Line = line
        self._counting: int = 0

    def do(self):
        trajectories: List[Trajectory] = self._inputs["trajectories"].get()
        if trajectories is not None:
            for trajectory in trajectories:
                # Examine all trajectories and check if they are crossing the line
                for pt1, pt2 in zip(self._line.points, self._line.points[:1]):
                    if self.is_intersecting(trajectory, (pt1.value(), pt2.value())):
                        print(trajectory.direction())

        if self._outputs["counting"].is_linked():
            self._outputs["counting"].set(self._counting)

        if self._outputs["line"].is_linked():
            self._outputs["line"].set(self._line)

    
    def is_intersecting(self, trajectory: Trajectory, segment):
        for point, point1 in zip(trajectory.points, trajectory.points[1:]):
            if intersects((point.value(), point1.value()), segment):
                return True
        return False