from typing import Dict, List, Tuple
from threading import Thread
from datetime import datetime
import os
from time import sleep

from lib.components.base_component import BaseComponent
from lib.components.thread_component import ThreadComponent
from lib.components.component import Component
from lib.models.links.link import Link

class Project(Component):
    def __init__(self, name="Project") -> None:
        super().__init__(name=name)

        self._components: Dict[str, BaseComponent] = {}
        self._links: List[Link] = []
        self._running: bool = True
        self._date: datetime = datetime.now()
        self._begin_time: datetime = None
        self._end_time: datetime = None
    
    def run(self):
        self._begin_time = datetime.now()
        try:
            [component.initiate() for component in self._components.values()]
            [component.start() for component in self._components.values()]
            while self._running:
                [component.run() for component in self._components.values()]
        except KeyboardInterrupt:
            self._running = False
            [component.stop() for component in self._components.values()]

        self._end_time = datetime.now()
        return self

    def run_threaded(self):
        self._begin_time = datetime.now()
        threads = [ThreadComponent(component.start()).begin() for component in self._components.values()]

        try:
            while self._running:
                sleep(1)
        except KeyboardInterrupt:
            self._running = False
            [thread.end() for thread in threads]

        self._end_time = datetime.now()
        return self
