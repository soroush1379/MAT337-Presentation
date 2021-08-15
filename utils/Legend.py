from enum import Enum

class Legend:
    def __init__(self):
        self.location = None
        self.fontSize = None
        self.columnNumber = None
        self.title = None

    def withLocation(self, location):
        self.location = location
        return self

    def withFontSize(self, fontSize: int):
        self.fontSize = fontSize
        return self

    def withColumnNumber(self, columnNumber: int):
        self.columnNumber = columnNumber
        return self

    def withTitle(self, title: str):
        self.title = title
        return self

    # GETTERS

    def getLocation(self) -> str:
        return Location.BEST.value if self.location is None else self.location.value

    def getFontSize(self) -> int:
        return self.fontSize

    def getColumnNumber(self) -> int:
        return 1 if self.columnNumber is None else self.columnNumber

    def getTitle(self) -> str:
        return self.title

class Location(Enum):
    BEST = "best"
    TOP_RIGHT = "upper right"
    TOP_LEFT = "upper left"
    BOTTOM_LEFT = "lower left"
    BOTTOM_RIGHT = "lower right"
    CENTER_RIGHT = "center right"
    CENTER_LEFT = "center left"
    BOTTOM_CENTER = "lower center"
    TOP_CENTER = "upper center"
    CENTER = "center"
