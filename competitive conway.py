import pygame
from pygame.locals import *
import time
#try pygame binary https://inventwithpython.com/pygame/chapter1.html
import setupConditions as sc
from Grid import Grid
from Window import Window
from Player import Player
from Button import Button

class Game():
    def __init__(self):
        self.player1 = Player(1)
        self.player1.button = Button(sc.windowMargin, sc.windowHeight - sc.windowMargin - sc.buttonHeight, sc.buttonWidth, sc.buttonHeight)
        self.player2 = Player(2)
        self.player2.button = Button(sc.windowWidth - sc.windowMargin - sc.buttonWidth, sc.windowHeight - sc.windowMargin - sc.buttonHeight, sc.buttonWidth, sc.buttonHeight)

        self.grid = Grid(sc.gridWidth, sc.gridHeight, sc.homeZoneWidth)
        self.grid.initialiseGridSquareDimensions(sc.windowWidth, sc.windowHeight, sc.windowMargin)
        self.grid.initialiseGrid(sc.windowMargin)
        self.grid.initialiseBases(self.player1, self.player2, sc.numBases, sc.baseSize, sc.baseSeparation)

        self.golCooldownTime = 0

        self.window = Window(sc.windowWidth, sc.windowHeight)
        self.window.initialiseWindow()

        self.playing = False

    def play(self): #gameloop
        self.playing = True
        self.window.displayWindow(self.grid, self)
        time.sleep(0.02)
        while self.playing:
            self.checkForWinner()
            self.window.eventGet()
            if self.window.screenClicked:
                self.screenClicked()
            if time.time() > self.golCooldownTime:
                self.getChanges()
                self.applyChanges()
                self.golCooldownTime = time.time() + 0.5
            self.window.displayWindow(self.grid, self)
            time.sleep(0.02)

    def screenClicked(self):
        x, y = pygame.mouse.get_pos()
        #has it clicked a gridsquare
        for gridSquare in self.grid.gridArray:
            if gridSquare.rect.collidepoint(x,y):
                #check it's not a base
                isBase = False
                for base in self.player1.bases:
                    if self.grid.calcArrayIndex(gridSquare.gridx, gridSquare.gridy) in base.gridIndexes:
                        isbase = True
                for base in self.player2.bases:
                    if self.grid.calcArrayIndex(gridSquare.gridx, gridSquare.gridy) in base.gridIndexes:
                        isBase = True
                if not isBase:
                    gridSquare.clicked()
                break
        #has it clicked a button
        if self.player1.button.rect.collidepoint(x,y):
            for gridSquare in self.grid.gridArray:
                if gridSquare.gridx < sc.homeZoneWidth and gridSquare.status == "Pending":
                    gridSquare.status = "Alive"
        elif self.player2.button.rect.collidepoint(x,y):
            for gridSquare in self.grid.gridArray:
                if gridSquare.gridx > (sc.gridWidth - sc.homeZoneWidth - 1) and gridSquare.status == "Pending":
                    gridSquare.status = "Alive"

    def getChanges(self): #possible changes: Live, Die, Maintain
        for gridSquare in self.grid.gridArray:
            gridSquare.checkNear(self.grid)
            if gridSquare.status == "Dead":
                if gridSquare.nearAlive == 3:
                    gridSquare.nextMove = "Live"
                else:
                    gridSquare.nextMove = "Maintain"
            elif gridSquare.status == "Alive":
                if gridSquare.nearAlive < 2 or gridSquare.nearAlive > 3:
                    gridSquare.nextMove = "Die"
                else:
                    gridSquare.nextMove = "Maintain"

    def applyChanges(self):
        for gridSquare in self.grid.gridArray:
            if gridSquare.nextMove == "Die":
                gridSquare.status = "Dead"
            elif gridSquare.nextMove == "Live":
                gridSquare.status = "Alive"

    def checkForWinner(self):
        #player1
        basesAlive = False
        for base in self.player1.bases:
            squaresAlive = 0
            for index in base.gridIndexes:
                if self.grid.gridArray[index].status == "Alive":
                    squaresAlive += 1
            if squaresAlive >= (len(base.gridIndexes) / 2):
                basesAlive = True
                break
        if not basesAlive:
            print("PLAYER 2 WINS")
            pygame.quit()
            quit()
        #player2
        basesAlive = False
        for base in self.player2.bases:
            squaresAlive = 0
            for index in base.gridIndexes:
                if self.grid.gridArray[index].status == "Alive":
                    squaresAlive += 1
            if squaresAlive >= (len(base.gridIndexes) / 2):
                basesAlive = True
                break
        if not basesAlive:
            print("PLAYER 1 WINS")
            pygame.quit()
            quit()

game = Game()
game.play()