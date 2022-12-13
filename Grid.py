from GridSquare import GridSquare
from Base import Base
import pygame
import math
class Grid():
    def __init__(self, gridWidth, gridHeight, homeZoneWidth):
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.homeZoneWidth = homeZoneWidth
        self.gridlines = []

    def calcArrayIndex(self, gridx, gridy):
        index = (gridy * self.gridWidth) + gridx
        return index

    def initialiseGridSquareDimensions(self, windowWidth, windowHeight, windowMargin):
        self.gsWidth = (windowWidth - (2*windowMargin)) / self.gridWidth
        self.gsHeight = (windowHeight - windowMargin - 200) / self.gridHeight

    def initialiseGrid(self, windowMargin): #across then down coordinates
        self.gridArray = []
        for i in range(self.gridHeight):
            for j in range(self.gridWidth):
                homeZone = False
                if j < self.homeZoneWidth or j > self.gridWidth - self.homeZoneWidth - 1:
                    homeZone = True
                newGridSquare = GridSquare(j, i, homeZone, self.gsWidth, self.gsHeight)
                newGridSquare.genCoords(windowMargin)
                self.gridArray.append(newGridSquare)
        self.createGridlines()

    def createGridlines(self):
        for i in range(self.gridWidth + 1):
            if i == self.homeZoneWidth or i == self.gridWidth - self.homeZoneWidth:
                lineWidth = 6
            else:
                lineWidth = 2
            self.gridlines.append(pygame.Rect(self.gridArray[0].x + (i * self.gsWidth) - (lineWidth/2), self.gridArray[0].y, lineWidth, self.gridHeight * self.gsHeight))
        for i in range(self.gridHeight + 1):
            self.gridlines.append(pygame.Rect(self.gridArray[0].x, self.gridArray[0].y + (i * self.gsHeight) - 1, self.gridWidth * self.gsWidth, 2))

    def initialiseBases(self, player1, player2, numBases, baseSize, baseSeparation):
        if baseSize == 2:
            baseHeight = 2
            baseWidth = 2
        elif baseSize == 3:
            baseHeight = 4
            baseWidth = 3
        elif baseSize == 4:
            baseHeight = 5
            baseWidth = 4
        yBuffer = math.floor((self.gridHeight - (baseSeparation * numBases) - (numBases * baseHeight)) / 2)

        for i in range(numBases):
            baseX = 1
            baseY = yBuffer + (baseSeparation * (i + 1)) + (i * baseHeight)
            base = Base(i, baseSize, baseX, baseY) #coords for top left square of rectangle area around base
            base.player = player1
            player1.bases.append(base)
        for i in range(numBases):
            baseX = self.gridWidth - baseWidth - 1
            baseY = yBuffer + (baseSeparation * (i + 1)) + (i * baseHeight)
            base = Base(i, baseSize, baseX, baseY) #coords for top left square of rectangle area around base
            base.player = player2
            player2.bases.append(base)
        self.addBasesToGrid(player1, player2)

    def addBasesToGrid(self, player1, player2):
        for base in player1.bases:
            base.addToGrid(self)
        for base in player2.bases:
            base.addToGrid(self)

