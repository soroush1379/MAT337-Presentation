from utils.Color import Color


class Trendline:
    x = list
    y = list
    name = str
    lineWidth = int
    lineStyle = str
    marker = str
    color = Color

    def __init__(self, x: list, y: list):
        if len(x) != len(y):
            raise AssertionError(
                "The length of the x and y arguments of a trendline need to be equal."
            )
        self.x = x
        self.y = y
        self.name = None
        self.lineWidth = None
        self.lineStyle = None
        self.marker = None
        self.color = None

    @classmethod
    def fromLambda(self, xvals: list, function):
        yvals = [function(x) for x in xvals]
        return Trendline(xvals, yvals)

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
