from lib.components.base_component import BaseComponent
from lib.models.links.inputs import Input
from lib.models.data.data import Data


class RequestComponent(BaseComponent):
    def __init__(self, host: str, port: int = None, ssl: str = "http", execution_mode: int = 1, name: str = None):
        super().__init__(execution_mode=execution_mode, name=name)
        self._host: str = host
        self._port: int = None
        self._ssl: str = ssl
        self._domain: str = f"{self._host}" if self._port is None else f"{self._host}:{self._port}"
        self._url: str = f"{self._ssl}://{self._domain}"

        self._inputs["data"] = Input()

    def initiate(self):
        return super().initiate()

    def do(self):
        # Receive the Data as an input
        data: Data = self._inputs["data"].get()

        # Check if the Data is not empty (including inside data (with required data))

        # If complete, the Data is beeing send to the API
        
        ...