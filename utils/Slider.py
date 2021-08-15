from enum import Enum
from utils.Color import Color
from utils.Label import Label


class Slider:
    min = float
    max = float
    value = float
    label = str
    orientation = None
    color = Color
    thickness = float # Percentage of figure length
    length = float # Percentage of figure length
    valueFormat = str # string format

    def __init__(self, min: float, max: float, initialValue: float):
        self.min = min
        self.max = max
        self.value = initialValue
        self.label = None
        self.orientation = None
        self.color = None
        self.thickness = None
        self.length = None
        self.valueFormat = None

    # GETTERS

    def getMin(self) -> float:
        return self.min

    def getMax(self) -> float:
        return self.max

    def getValue(self) -> float:
        return self.value

    def getLabel(self) -> Label:
        return self.label

    def getOrientation(self) -> str:
        return (
            Orientation.HORIZONTAL.value
            if self.orientation is None
            else self.orientation.value
        )

    def getColor(self) -> str:
        return self.color

    def getThickness(self) -> float:
        return 0.05 if self.thickness is None else self.thickness

    def getLength(self) -> float:
        return 0.6 if self.length is None else self.length

    def getValueFormat(self) -> str:
        return self.valueFormat

    # SETTERS

    def setValue(self, value: float) -> None:
        self.value = value

    def withLabel(self, label: Label):
        self.label = label
        return self

    def withOrientation(self, orientation):
        self.orientation = orientation
        return self

    def withColor(self, color: Color):
        self.color = color
        return self

    def withThickness(self, thickness: float):
        self.thickness = thickness
        return self

    def withLength(self, length: float):
        self.length = length
        return self

    def withValueFormat(self, valueFormat: str) -> str:
        self.valueFormat = valueFormat
        return self


class Orientation(Enum):
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"
