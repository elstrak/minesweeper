import pygame
import os
from time import sleep


class Game():  # represent user interface
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.cellSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.loadImages()

    def run(self):  # initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)  # screen
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
            self.draw()
            pygame.display.flip()
            if self.board.getWon():
                sound = pygame.mixer.Sound("win.mp3")
                sound.play()
                sleep(3)
                running = False
        pygame.quit()
    def draw(self): # draw the board
        topLeft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                cell = self.board.getCell((row,col))
                image = self.getImage(cell)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.cellSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.cellSize[1]

    def loadImages(self):
        self.images = {}
        for fileName in os.listdir("images"):
            if (not fileName.endswith(".png")):
                continue
            image = pygame.image.load("images/" + fileName)
            image = pygame.transform.scale(image, self.cellSize)
            self.images[fileName.split(".")[0]] = image

    def getImage(self, cell):
        string = None
        if (cell.getClicked()):
            string = "bomb-at-clicked-block" if cell.getHasBomb() else str(cell.getNumAround())
        else:
            string = "flag" if cell.getFlagged() else "empty-block"
        return self.images[string]

    def handleClick(self, position, rightClick):
        if self.board.getLost():
            return
        index = position[1] // self.cellSize[1], position[0] // self.cellSize[0]
        cell = self.board.getCell(index)
        self.board.handleClick(cell, rightClick)

