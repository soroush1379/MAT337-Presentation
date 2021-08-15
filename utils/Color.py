class Color:
    def __init__(self, red: float, green: float, blue: float):
        self.red = red
        self.green = green
        self.blue = blue

    # Setters

    def getRed(self, red: float) -> None:
        self.red = red

    def getGreen(self, green: float) -> None:
        self.green = green

    def getBlue(self, blue: float) -> None:
        self.blue = blue

    # Getters

    def getRed(self) -> float:
        return self.red

    def getGreen(self) -> float:
        return self.green

    def getBlue(self) -> float:
        return self.blue
