import math

def readfile():
    with open('day8input.txt', 'r') as grid:
        grid = grid.readlines()
    strippedGrid = []
    for string in grid:
        strippedString = string.strip('\n')
        strippedGrid.append(strippedString)
    return strippedGrid

def gridDimensions(strippedGrid):
    gridDimensions = {}
    gridDimensions["Max Row"] = len(strippedGrid)-1
    gridDimensions["Max Column"] = len(strippedGrid[0])-1
    return gridDimensions

class Tree():
    _registry = []

    def __init__(self, row, column, height, visible):
        self.row = row
        self.column = column
        self.height = height
        self.visible = visible
        self._registry.append(self)

    def printTreeDetails(self):
        print(f"Tree at row {self.row}, column {self.column} (height: {str(self.height)}/{str(self.visible)})")

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def get_height(self):
        return self.height

    def get_visible(self):
        return self.visible
    
    def set_visible(self, visible):
        self.visible = visible

def instantiateTrees(grid):
    row = 0
    while row < len(grid):
        column = 0
        while column < len(grid[row]):
            visible = "Unknown"
            if row == 0 or row == len(grid)-1 or column == 0 or column == len(grid[row])-1:
                visible = True
            Tree(row, column, grid[row][column], visible)
            column += 1
        row += 1

def calculateIndex(row, column, numColumns):
    index = 0
    fullRows = ((numColumns+1)*row)
    partialRow = column+1
    index += fullRows+partialRow-1
    return index

def seeTrees(gridDimensions):
    numVisible = 0
    for tree in Tree._registry:
        tree.printTreeDetails()
        if tree.get_visible() == True:
            numVisible += 1
    print("Num Visible: ", numVisible)

def getUnknownVisible(gridDimensions):
    unknownVisible = []
    for tree in Tree._registry:
        if tree.get_visible() == 'Unknown':
            unknownVisible.append(calculateIndex(tree.get_row(), tree.get_column(), gridDimensions["Max Column"]))
    return unknownVisible

def getComparisonIndices(gridDimensions, index):
    compare = {}
    rowLength = gridDimensions["Max Column"]+1
    columnHeight = gridDimensions["Max Column"]+1
    numTrees = (rowLength*columnHeight)
    compareUp = []
    compareDown = []
    compareLeft = []
    compareRight = []
    currentRow = math.floor(index/rowLength) #assumes first row is 1

    #check left
    nextIndex = index - 1
    nextRow = math.floor(nextIndex/rowLength)
    while nextRow == currentRow:
        compareLeft.append(nextIndex)
        nextIndex -= 1
        nextRow = math.floor(nextIndex/rowLength)
    
    # check right
    nextIndex = index + 1
    nextRow = math.floor(nextIndex/rowLength)
    while nextRow == currentRow:
        compareRight.append(nextIndex)
        nextIndex += 1
        nextRow = math.floor(nextIndex/rowLength)
    
    # check up
    nextIndex = index - rowLength
    while nextIndex >= 0:
        compareUp.append(nextIndex)
        nextIndex = nextIndex - rowLength

    # check down
    nextIndex = index + rowLength
    while nextIndex < numTrees:
        compareDown.append(nextIndex)
        nextIndex = nextIndex + rowLength

    compare['left'] = compareLeft
    compare['right'] = compareRight
    compare['up'] = compareUp
    compare['down'] = compareDown

    return compare

def determineVisibility(unknownVisible, gridDimensions):
    for index in unknownVisible:
        tree = Tree._registry[index]
        treeHeight = tree.get_height()
        compare = getComparisonIndices(gridDimensions, index)
        visibleFromTop = True
        visibleFromBottom = True
        visibleFromLeft = True
        visibleFromRight = True

        for i in compare['up']:
            comparisonTree = Tree._registry[i]
            if comparisonTree.get_height() >= treeHeight:
                visibleFromTop = False
        for i in compare['down']:
            comparisonTree = Tree._registry[i]
            if comparisonTree.get_height() >= treeHeight:
                visibleFromBottom = False
        for i in compare['right']:
            comparisonTree = Tree._registry[i]
            if comparisonTree.get_height() >= treeHeight:
                visibleFromRight = False
        for i in compare['left']:
            comparisonTree = Tree._registry[i]
            if comparisonTree.get_height() >= treeHeight:
                visibleFromLeft = False
        
        if visibleFromTop or visibleFromBottom or visibleFromRight or visibleFromLeft:
            tree.set_visible(True)
        else:
            tree.set_visible(False)

grid = readfile()
gridDimensions = gridDimensions(grid)
trees = instantiateTrees(grid)
seeTrees(gridDimensions)
unknownVisible = getUnknownVisible(gridDimensions)
determineVisibility(unknownVisible, gridDimensions)
seeTrees(gridDimensions)