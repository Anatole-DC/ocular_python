from typing import Dict, List

from lib.components.annotations.draw import DrawComponent
from lib.components.base_component import BaseComponent
from lib.components.capture.video import VideoComponent
from lib.components.streamer.webstreamer import WebStreamerComponent
from lib.components.streamer.displayer import DisplayerComponent
from lib.models.links.link import Link
from lib.components.tracking.hungarian_tracker import HungarianTrackerComponent
from lib.components.detection.pose_detection import PoseDetectorComponent
from lib.components.detection.yolov5_detector import YoloV5DetectorComponent
from lib.components.tracking.pose_identity_tracker import PoseIdentityTrackerComponent
from lib.projects.project import Project
from lib.projects.performance.report import Report


def main():

    project = Project()

    components: Dict[str, BaseComponent] = {
        "camera": VideoComponent(
            "/home/anatole/IVS/Projects/IVSLite/evaluation/gosport/35/2022-12-19_15_14_58.mp4",
            frame_interval=(0, 2500),
            # scale=1
        ),
        # "ball_detector": YoloV5DetectorComponent(
        #     "/data/models/ocular/basketball_detector_1920.pt"
        # ),
        # "draw": DrawComponent(),
        "displayer": WebStreamerComponent("0.0.0.0")
    }

    # Setup all links

    links: List[Link] = [
        Link()
        .entrypoint(components["camera"], "frames")
        .destination(components["displayer"], "frames"),

        # Link()
        # .entrypoint(components["camera"], "frames")
        # .destination(components["draw"], "frames"),

        # Link()
        # .entrypoint(components["ball_detector"], "detections")
        # .destination(components["draw"], "elements"),

        # Link()
        # .entrypoint(components["draw"], "frames")
        # .destination(components["displayer"], "frames"),
    ]

    project._components = components
    project._links = links

    project.run()

    # Report(project, "temp").build().export()

    print("Exiting the program......")


if __name__ == "__main__":
    main()
