from utils.Color import Color
from utils.Slider import Slider


class TrendlineInteractive:
    x = list
    func = None  # A function
    sliders = list
    textboxes = list
    name = str
    lineWidth = int
    lineStyle = str
    marker = str
    color = Color

    def __init__(self, x: list, func, sliders: list, textboxes: list):
        self.x = x
        self.func = func
        self.sliders = sliders
        self.textboxes = textboxes
        self.name = None
        self.lineWidth = None
        self.lineStyle = None
        self.marker = None
        self.color = None

    def withName(self, name: str):
        self.name = name
        return self

    def withLineWidth(self, lineWidth: float):
        self.lineWidth = lineWidth
        return self

    def withLineStyle(self, lineStyle: str):
        self.lineStyle = lineStyle
        return self

    def withMarker(self, marer: str):
        self.marker = marker
        return self

    def withColor(self, color: Color):
        self.color = color
        return self

    # GETTERS

    def getX(self) -> list:
        return self.x

    def getY(self) -> list:
        valueList = [s.getValue() for s in self.sliders + self.textboxes]
        return [self.func(xval, *valueList) for xval in self.x]

    def getTextboxes(self):
        return self.textboxes

    def getTextbox(self, index: int):
        if index < 0 or index > len(self.textboxes):
            raise AssertionError(
                "Asked to retrieve a non-existent textbox in trendline interactive."
            )
        return self.textboxes[index]

    def getSliders(self):
        return self.sliders

    def getSlider(self, index: int):
        if index < 0 or index > len(self.sliders):
            raise AssertionError(
                "Asked to retrieve a non-existent slide in trendline interactive."
            )
        return self.sliders[index]

    def getFunction(self) -> list:
        return self.y

    def getName(self) -> str:
        return self.name

    def getLineWidth(self) -> int:
        return self.lineWidth

    def getLineStyle(self) -> str:
        return self.lineStyle

    def getMarker(self) -> str:
        return self.marker

    def getColor(self) -> Color:
        return self.color
