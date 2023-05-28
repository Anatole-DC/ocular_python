from lib.components.capture.base_capture_component import BaseCaptureComponent


class CameraComponent(BaseCaptureComponent):
    def __init__(self, channel: int = 0, scale: float = 1.0, execution_mode: int = 1, name: str = "WebcamComponent"):
        super().__init__(channel=channel, scale=scale, execution_mode=execution_mode, name=name)
