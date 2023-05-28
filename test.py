from typing import Dict, List
import json

from lib.components.annotations.draw import DrawComponent
from lib.components.base_component import BaseComponent
from lib.components.capture.video import VideoComponent
from lib.components.streamer.webstreamer import WebStreamerComponent
from lib.components.streamer.displayer import DisplayerComponent
from lib.models.links.link import Link
from lib.components.tracking.hungarian_tracker import HungarianTrackerComponent
from lib.components.detection.pose_detection import PoseDetectorComponent
from lib.projects.project import Project
from lib.projects.performance.report import Report
from lib.components.capture.recorder import RecorderComponent

from src.data.players import player_data


def main():

    project = Project()

    components: Dict[str, BaseComponent] = {
        "camera": VideoComponent(
            "assets/videos/basketball_game_high_angle.mp4",
            frame_interval=(0, 7500)
        ),
        "displayer": DisplayerComponent()
    }

    # Setup all links

    links: List[Link] = [
        Link()
        .entrypoint(components["camera"], "frames")
        .destination(components["displayer"], "frames"),
    ]

    project._components = components
    project._links = links

    project.run()

    # Report(project, "temp").build().export()

    print("Exiting the program......")


if __name__ == "__main__":
    main()
    ...
