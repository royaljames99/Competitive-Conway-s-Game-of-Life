class Base():
    def __init__(self, index, baseSize, gridx, gridy):
        self.index = index
        self.baseSize = baseSize
        self.gridx = gridx
        self.gridy = gridy
        self.gridIndexes = []

    def addToGrid(self, grid):
        if self.baseSize == 2:
            self.gridIndexes = [grid.calcArrayIndex(self.gridx, self.gridy), grid.calcArrayIndex(self.gridx + 1, self.gridy), grid.calcArrayIndex(self.gridx, self.gridy + 1), grid.calcArrayIndex(self.gridx + 1, self.gridy + 1)]
        elif self.baseSize == 3:
            self.gridIndexes = [grid.calcArrayIndex(self.gridx + 1, self.gridy), grid.calcArrayIndex(self.gridx, self.gridy + 1), grid.calcArrayIndex(self.gridx + 2, self.gridy + 1), grid.calcArrayIndex(self.gridx, self.gridy + 2), grid.calcArrayIndex(self.gridx + 2, self.gridy + 2), grid.calcArrayIndex(self.gridx + 1, self.gridy + 3)]
        elif self.baseSize == 4:
            self.gridIndexes = [grid.calcArrayIndex(self.gridx + 1, self.gridy), grid.calcArrayIndex(self.gridx + 2, self.gridy), grid.calcArrayIndex(self.gridx, self.gridy + 1), grid.calcArrayIndex(self.gridx + 3, self.gridy + 1), grid.calcArrayIndex(self.gridx + 1, self.gridy + 2), grid.calcArrayIndex(self.gridx + 3, self.gridy + 2), grid.calcArrayIndex(self.gridx + 2, self.gridy + 3)]
        for i in self.gridIndexes:
            grid.gridArray[i].status = "Alive"