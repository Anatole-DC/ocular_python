from typing import Tuple, List, Dict
from random import randint

from lib.components.base_component import BaseComponent
from lib.models.links.inputs import Input
from lib.models.links.outputs import Output
from lib.models.pose import Pose


MIN_IDENTITY_SCORE_DISTANCE: float = 0.0


class PoseIdentityTrackerComponent(BaseComponent):
    def __init__(self, name: str = "PoseIdentityTrackerComponent"):
        super().__init__(name=name)
        self._inputs["poses"] = Input()
        self._inputs["frames"] = Input()
        self._outputs["frames"] = Output()
        self._POSE_IDENTITY_BUFFER: List[Dict] = [
            {
                "player": "uid",
                "scores": [0.0, 0.0, 0.0, 0.0, 0.0]
            }
        ]

    def compute_identity_score(self, pose: Pose) -> List[float]:
        return []

    def compute_detection_distance(self, score: List[float]) -> Tuple[int, float]:
        return (0, 0.0)

    def generate_uid(self) -> int:
        return int("".join([randint(0, 9) for _ in range(9)]))

    def do(self):
        detections: List[Pose] = self._inputs["poses"].get()

        if detections is not None:
            scores: List[List[float]] = []  # All the scores for each detection
            for pose in detections:
                scores.append(self.compute_identity_score(pose))

            for score in scores:
                closest_detection_index, closest_detection_score = self.compute_detection_distance(score)

                if closest_detection_score <= MIN_IDENTITY_SCORE_DISTANCE:
                    self._POSE_IDENTITY_BUFFER[closest_detection_index]["scores"] = score
                else:
                    self._POSE_IDENTITY_BUFFER.append({
                        "player": self.generate_uid(),
                        "scores": score
                    })

            if self._outputs["frames"].is_linked():
                frame = self._inputs["frames"].get()
                [detection.draw(frame.image) for detection in detections]
                self._outputs["frames"].set(frame)
