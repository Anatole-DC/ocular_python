from typing import Dict
from datetime import datetime
from random import randint

class Data:

    def __init__(self, value = None, data = {}, label: str = None) -> None:
        self._label: str = "".join([str(randint(0, 9)) for _ in range(8)])
        self._value = value
        self._data: Dict[str, Data] = data

    @property
    def value(self):
        return self._value

    def is_empty(self):
        return self._value is None

    def json(self):
        return {key: value.json() for key, value in self._data.items()}


class TimestampData(Data):
    ...

class IntData(Data):
    def json(self):
        return self._value
    
class BBoxData(Data):
    ...

class ChoiceData(Data):
    ...

class ROIData(Data):
    ...

class FrameData(Data):
    ...

class Base64Data:
    ...

class UIDData(Data):
    ...

class StringData(Data):
    def json(self):
        return self._value

class PostureData(Data):
    ...

class PositionData(Data):
    ...
