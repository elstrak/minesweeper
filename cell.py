
class Cell():
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False

    def getHasBomb(self):
        return self.hasBomb

    def getClicked(self):
        return self.clicked

    def getFlagged(self):
        return self.flagged

    def setNeighbours(self, neighbours):
        self.neighbours = neighbours
        self.setNumAround()

    def setNumAround(self):
        numAround = 0
        for cell in self.neighbours:
            if cell.getHasBomb():
                numAround += 1
        self.numAround = numAround

    def getNumAround(self):
        return self.numAround

    def toggleFlag(self):
        self.flagged = not self.flagged

    def click(self):
        self.clicked = True

    def getNeighbours(self):
        return self.neighbours