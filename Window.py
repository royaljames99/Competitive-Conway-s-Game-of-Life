import pygame
from pygame.locals import *
class Window():
    def __init__(self, windowWidth, windowHeight):
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.screenClicked = False

    def initialiseWindow(self):
        pygame.init()
        self.windowSurface = pygame.display.set_mode((self.windowWidth, self.windowHeight), 0, 32)
        pygame.display.set_caption("Competitive Conway")

    def eventGet(self):
        self.screenClicked = False
        for event in pygame.event.get():
            #detect screen close
            if event.type == QUIT:
                pygame.quit()
                quit()
            #detect screen click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.screenClicked = True

    def fillScreen(self, rgb):
        self.windowSurface.fill(rgb)

    def displayWindow(self, grid, game):
        self.fillScreen((0,0,0))
        self.displayGrid(grid, game)
        pygame.draw.rect(self.windowSurface, (255,255,255), game.player1.button)
        pygame.draw.rect(self.windowSurface, (255,255,255), game.player2.button)
        pygame.display.update()

    def displayGrid(self, grid, game):
        self.assembleGridRects(grid)
        for gridSquare in grid.gridArray:
            #handle bases first
            found = False
            index = grid.calcArrayIndex(gridSquare.gridx, gridSquare.gridy) 
            for base in game.player1.bases:
                if index in base.gridIndexes:
                    found = True
                    if gridSquare.status == "Alive":
                        colour = (0,120,255)
                    else:
                        colour = (255,120,0)
            for base in game.player2.bases:
                if index in base.gridIndexes:
                    found = True
                    if gridSquare.status == "Alive":
                        colour = (0,120,255)
                    else:
                        colour = (255,120,0)
            #not bases
            if not found:
                if gridSquare.status == "Alive":
                    colour = (255,255,255)
                elif gridSquare.status == "Pending":
                    colour = (150,150,50)
                else:
                    colour = (50,50,50)
            pygame.draw.rect(self.windowSurface, colour, gridSquare.rect)
        for gridline in grid.gridlines:
            pygame.draw.rect(self.windowSurface, (30,30,30), gridline)
    
    def assembleGridRects(self, grid): #pygame rectangle objects
        for gridSquare in grid.gridArray:
            gridSquare.rect = pygame.Rect(gridSquare.x, gridSquare.y, gridSquare.gsWidth, gridSquare.gsHeight)

        
