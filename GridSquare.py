class GridSquare():
    def __init__(self, gridx, gridy, homeZone, gsWidth, gsHeight):
        self.gridx = gridx
        self.gridy = gridy
        self.x = 0
        self.y = 0
        self.status = "Dead" #possible statuses: Dead, Alive, Pending
        self.nearAlive = 0
        self.nextMove = "Maintain"
        self.homeZone = homeZone
        self.gsWidth = gsWidth
        self.gsHeight = gsHeight
        self.rect = None

    def genCoords(self, margin): #coords of top left of gridsquare
        self.x = margin + (self.gsWidth * self.gridx)
        self.y = margin + (self.gsHeight * self.gridy)

    def clicked(self):
        if self.homeZone:
            if self.status == "Dead":
                self.status = "Pending"
            elif self.status == "Pending":
                self.status = "Dead"

    def checkNear(self, grid):
        self.nearAlive = 0
        #squares above
        if self.gridy != 0:
            if grid.gridArray[grid.calcArrayIndex(self.gridx, self.gridy - 1)].status == "Alive":
                self.nearAlive += 1
            if self.gridx != grid.gridWidth - 1:
                if grid.gridArray[grid.calcArrayIndex(self.gridx + 1, self.gridy - 1)].status == "Alive":
                    self.nearAlive += 1
            if self.gridx != 0:
                if grid.gridArray[grid.calcArrayIndex(self.gridx - 1, self.gridy - 1)].status == "Alive":
                    self.nearAlive += 1
        #square left
        if self.gridx != 0:
            if grid.gridArray[grid.calcArrayIndex(self.gridx - 1, self.gridy)].status == "Alive":
                self.nearAlive += 1
        #square right
        if self.gridx != grid.gridWidth - 1:
            if grid.gridArray[grid.calcArrayIndex(self.gridx + 1, self.gridy)].status == "Alive":
                self.nearAlive += 1
        #squares below
        if self.gridy != grid.gridHeight - 1:
            if grid.gridArray[grid.calcArrayIndex(self.gridx, self.gridy + 1)].status == "Alive":
                self.nearAlive += 1
            if self.gridx != grid.gridWidth - 1:
                if grid.gridArray[grid.calcArrayIndex(self.gridx + 1, self.gridy + 1)].status == "Alive":
                    self.nearAlive += 1
            if self.gridx != 0:
                if grid.gridArray[grid.calcArrayIndex(self.gridx - 1, self.gridy + 1)].status == "Alive":
                    self.nearAlive += 1
