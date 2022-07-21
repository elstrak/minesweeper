from cell import Cell
from random import random

class Board(): # creating a game board
    def __init__(self, size, prob):
        self.size = size # board size
        self.prob = prob # chance of a bomb in a cell
        self.lost = False
        self.won = False
        self.numClicked = 0
        self.numNonBombs = 0
        self.setBoard()
    def setBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                hasBomb = random() < self.prob
                if (not hasBomb):
                    self.numNonBombs += 1
                cell = Cell(hasBomb) # individual cell on the board
                row.append(cell)
            self.board.append(row)
        self.setNeighbours()

    def setNeighbours(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                cell = self.getCell((row, col))
                neighbours = self.getListOfNeighbours((row, col))
                cell.setNeighbours(neighbours)

    def getListOfNeighbours(self, index):
        neighbours = []
        for row in range(index[0] - 1, index[0] + 2):
            for col in range(index[1] - 1, index[1] + 2):
                outOfBounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                same = row == index[0] and col == index[1]
                if (same or outOfBounds):
                    continue
                neighbours.append(self.getCell((row, col)))
        return neighbours

    def getSize(self):
        return self.size

    def getCell(self, index):
        return self.board[index[0]][index[1]]

    def handleClick(self, cell, flag):
        if (cell.getClicked() or (not flag and cell.getFlagged())):
            return
        if flag:
            cell.toggleFlag()
            return
        cell.click()
        if (cell.getHasBomb()):
            self.lost = True
            return
        self.numClicked += 1
        if (cell.getNumAround() != 0):
            return
        for neighbour in cell.getNeighbours():
            if not neighbour.getHasBomb() and not neighbour.getClicked():
                self.handleClick(neighbour, False)

    def getLost(self):
        return self.lost

    def getWon(self):
        return self.numNonBombs == self.numClicked