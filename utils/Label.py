class Label:
    def __init__(self, title: str, fontSize: int):
        self.title = title
        self.fontSize = fontSize

    def getTitle(self) -> str:
        return self.title

    def getFontSize(self) -> int:
        return self.fontSize
