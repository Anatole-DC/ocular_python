from typing import Dict, Generator, Any, List, Tuple

from lib.components.base_component import BaseComponent, ExecutionErrorException, HamperedExecutionException
from lib.models.frame import Frame


class StorageMode:
    BUFFER: int = 0
    FLOW: int = 1


class Link:
    def __init__(self,
                 from_component: BaseComponent = None,
                 to_component: BaseComponent = None,
                 storage_mode: int = StorageMode.FLOW
                 ):
        self._from_component: BaseComponent = from_component
        self._to_component: BaseComponent = to_component
        self._storage_mode: int = storage_mode

        self._DATA_BUFFER = []

    def flow_storage(self, value):
        self._DATA_BUFFER = [value]

    def buffer_storage(self, value):
        self._DATA_BUFFER.append(value)

    def set(self, value):
        [
            self.flow_storage,
            self.buffer_storage
        ][self._storage_mode](value)

    def get(self):
        if self._DATA_BUFFER:
            output = self._DATA_BUFFER[0]
            self._DATA_BUFFER.pop(0)
            return output
        return None

    def is_linked(self) -> bool:
        return self._to_component is not None

    def is_provided(self) -> bool:
        return self._from_component is not None

    def is_complete(self) -> bool:
        return self.is_linked() and self.is_provided()

    def entrypoint(self, component: BaseComponent, value: str):
        try:
            self._from_component = component
            self._from_component.outputs[value].set_link(self)
            return self
        except KeyError:
            print(f"ERROR >>> Component {component} does not have output value {value}")
            return self

    def destination(self, component: BaseComponent, value: str):
        try:
            self._to_component = component
            self._to_component.inputs[value].set_link(self)
            return self
        except KeyError:
            print(f"ERROR >>> Component {component} does not have input value {value}")
            return self
