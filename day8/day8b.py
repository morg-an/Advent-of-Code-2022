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

    def __init__(self, row, column, height):
        self.row = row
        self.column = column
        self.height = int(height)
        self._registry.append(self)

    def printTreeDetails(self):
        print(f"Tree at row {self.row}, column {self.column} (height: {str(self.height)})")

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def get_height(self):
        return self.height

def instantiateTrees(grid):
    row = 0
    while row < len(grid):
        column = 0
        while column < len(grid[row]):
            Tree(row, column, grid[row][column])
            column += 1
        row += 1

def calculateIndex(row, column, numColumns):
    index = 0
    fullRows = ((numColumns+1)*row)
    partialRow = column+1
    index += fullRows+partialRow-1
    return index

def seeTrees(gridDimensions):
    for tree in Tree._registry:
        tree.printTreeDetails()

def lookUp(index, tree, trees, gridDimensions):
    nextIndex = index
    visibleTrees = 0
    rowWidth = gridDimensions["Max Column"]+1
    treeHeight = tree.get_height()
    treesUp = math.floor((index+1)/rowWidth)
    print("trees above - ", treesUp)
    i = 0
    while i < treesUp:
        nextIndex = nextIndex-rowWidth
        nextTreeHeight = trees[nextIndex].get_height()
        visibleTrees += 1
        if nextTreeHeight >= treeHeight:
            break
        i += 1
    print(f"Trees visible Above: {visibleTrees}")
    return visibleTrees

def lookDown(index, tree, trees, gridDimensions):
    nextIndex = index
    visibleTrees = 0
    rowWidth = gridDimensions["Max Column"]+1
    treeHeight = tree.get_height()
    treesDown = gridDimensions["Max Column"]-math.floor((index+1)/rowWidth)
    i = 0
    while i < treesDown:
        nextIndex = nextIndex+rowWidth
        nextTreeHeight = trees[nextIndex].get_height()
        visibleTrees += 1
        if nextTreeHeight >= treeHeight:
            break
        i += 1
    print(f"Trees visible Below: {visibleTrees}")
    return visibleTrees

def lookRight(index, tree, trees, gridDimensions):
    nextIndex = index
    visibleTrees = 0
    rowWidth = gridDimensions["Max Column"]+1
    treeHeight = tree.get_height()
    treesRight = rowWidth - (index % rowWidth) - 1
    i = 0
    while i < treesRight:
        nextIndex = nextIndex+1
        nextTreeHeight = trees[nextIndex].get_height()
        visibleTrees += 1
        if nextTreeHeight >= treeHeight:
            break
        i += 1
    print(f"Trees visible to the Right: {visibleTrees}")
    return visibleTrees

def lookLeft(index, tree, trees, gridDimensions):
    nextIndex = index
    visibleTrees = 0
    rowWidth = gridDimensions["Max Column"]+1
    treeHeight = tree.get_height()
    treesLeft = index % rowWidth
    i = 0
    while i < treesLeft:
        nextIndex = nextIndex-1
        nextTreeHeight = trees[nextIndex].get_height()
        visibleTrees += 1
        if nextTreeHeight >= treeHeight:
            break
        i += 1
    #print("Trees visible to Left: ", visibleTrees)
    print(f"Trees visible to the Right: {visibleTrees}")
    return visibleTrees

def calcScenicScore(index, tree, trees, gridDimensions):
    scenicScore = (lookUp(index, tree, trees, gridDimensions)*
        lookDown(index, tree, trees, gridDimensions)*
        lookRight(index, tree, trees, gridDimensions)*
        lookLeft(index, tree, trees, gridDimensions))
    print("Score:", scenicScore)
    return scenicScore

def findBestTree(trees, gridDimensions):
    highestScore = 0
    print("Num Trees", len(trees))
    i = 0
    while i < len(trees):
        index = i
        print(f"Checking Tree at Index {index}")
        tree = Tree._registry[i]
        score = calcScenicScore(index, tree, trees, gridDimensions)
        if score > highestScore:
            highestScore = score
        i += 1
    return highestScore

grid = readfile()

# determines the size of the forest (max row and column, returned as dict (keys: "Max Row" ; "Max Column"))
gridDimensions = gridDimensions(grid)
print(gridDimensions)

# loops through each row and column of grid file and create new Tree object for each value
instantiateTrees(grid)

# set 'trees' variable equal to list containing all Tree instances
trees = Tree._registry

#seeTrees(gridDimensions)

# returns the highest scenic score; findBestTrees calls calculateScenicScore() on each Tree instance, which in tern calls lookUp(), lookDown(), lookLeft(), and lookRight()
answer = findBestTree(trees, gridDimensions)

print("Answer:", answer)