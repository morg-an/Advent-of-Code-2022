import pygame
import math
from queue import PriorityQueue

colors = {'WHITE':(255, 255, 255), 'a':(237, 237, 237), 'b':(226, 227, 229), 'c': (213, 214, 216),
'd':(201, 202, 204), 'e':(193, 194, 196), 'f':(184, 185, 190), 'g':(177, 178, 183),
'h': (168, 169, 174), 'i':(160, 161, 166), 'j':(152, 153, 158), 'k': (144, 145, 150),
'l':(136, 137, 142), 'm':(129, 130, 135), 'n':(121, 122, 127), 'o':(117, 118, 123),
'p':(109, 110, 115), 'q': (105, 106, 108), 'r': (97, 97, 99), 's':(88, 88, 90), 
't':(79, 79, 81), 'u':(70, 70, 72), 'v':(56, 56, 58), 'w':(45, 45, 47), 'x':(34, 34, 36), 
'y':(22, 22, 24), 'z':(11, 11, 11),'BLACK':(0, 0, 0), 'GREEN':(171, 247, 177), 'PURPLE':(52, 0, 61)}

def readFile():
    with open('day12sample.txt', "r") as rawHeightMap:
        heightMap = rawHeightMap.readlines()
        for i in range(len(heightMap)):
            heightMap[i] = heightMap[i].strip()
    return heightMap

def main():
    heightMap = readFile() #parce input file
    display = drawDisplay(heightMap) #returns [window, width, height]
    window = display[0]
    width = display[1]
    height = display[2]
    keyNodes = generateNodes(heightMap, width, height)

    start = keyNodes[0]
    end = keyNodes[1]

    findPath(Node.grid, start, end)
    run = True
    started = False

    while run:
        draw(window, heightMap, width, height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started: #eventually will use to prevent user input while algorithm is running
                continue

    pygame.quit()

def generateNodes(heightMap, width, height):
    rows = len(heightMap)
    columns = len(heightMap[0])
    nodeWidth = width//columns
    nodeHeight = height//rows
    start = ""
    end = ""
    for i in range(rows):
        Node.grid.append([])
    for i in range(rows):
        rowContents = heightMap[i]
        for j in range(len(rowContents)): #iterate columns - left to right
            node = Node(rows-i-1, j, rows, columns, rowContents[j], nodeWidth, nodeHeight)
            if rowContents[j] in colors:
                node.color = colors[rowContents[j]]
            elif rowContents[j] == 'S':
                node.start = True
                node.elev = 'a'
                node.color = colors['GREEN']
                start = node
            elif rowContents[j] == 'E':
                node.end = True
                node.elev = 'z'
                node.color = colors['PURPLE']
                end = node
    return (start, end)

def drawDisplay(heightMap):
    targetHeight = 500
    targetWidth = 800
    excessHeight = targetHeight % len(heightMap)
    excessWidth = targetWidth % len(heightMap[0])
    height = targetHeight - excessHeight
    width = targetWidth - excessWidth
    
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Hill Climbing Algorithm")
    return [window, width, height]

def drawGridLines(window, width, height, rows, columns):
    nodeWidth = width//columns
    nodeHeight = height//rows
    for i in range(rows):
        pygame.draw.line(window, colors['BLACK'], (0, nodeHeight*i), (width, nodeHeight*i))
        for j in range(columns):
            pygame.draw.line(window, colors['BLACK'], (nodeWidth*j, 0), (nodeWidth*j, height))

def draw(window, heightMap, width, height):
    rows = len(heightMap)
    columns = len(heightMap[0])

    # fill entire background
    window.fill(colors['WHITE'])
    
    # draw the nodes
    for row in Node.grid:
        for node in row:
            node.draw(window)
    
    # draw the grid
    drawGridLines(window, width, height, rows, columns)

    #update display
    pygame.display.update()

def estimateDistance(p1, p2):
    #stimate the distance between two points
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)
    pass

def findPath(grid, start, end):
    minSteps = 0
    priorityList = []
    priorityList.append(start)
    adjacent = getAdjacent(priorityList[0])
    print(adjacent)

    return minSteps

def getAdjacent(node):
    adjacent = {}
    print('current: ', node, ord(node.elev.lower()))
    currentElev = ord(node.elev.lower())
    if node.right != None:
        print('right: ', ord(node.right.elev.lower()))
        if ord(node.right.elev.lower())-currentElev <= 1:
            adjacent['right'] = node.right
            print('adjacent:', adjacent)
    if node.left != None:
        if ord(node.left.elev.lower())-currentElev <= 1:
            adjacent['left'] = node.left
    if node.above != None:
        if ord(node.above.elev.lower())-currentElev <= 1:
            adjacent['above'] = node.above
    if node.below != None:
        if ord(node.below.elev.lower())-currentElev <= 1:
            adjacent['below'] = node.below
    return adjacent

class Node:
    grid = []

    def __init__(self, row, col, numRows, numColumns, elev, width, height, start = False, end = False):
        self.row = row
        self.col = col
        self.elev = elev
        self.width = width
        self.height = height
        self.xCoord = col * width
        self.yCoord = abs(row-(numRows-1)) * height
        self.color = colors['WHITE']
        self.start = start
        self.end = end
        self.below = None
        self.right = None
        # if not in top row, set self.above for current tile and self.below for tile directly above self.
        if row == numRows - 1:
            self.above = None
        else:
            self.above = Node.grid[row+1][col]
            Node.grid[row+1][col].below = self            
        # if not in first column, set self.left to node on left and self.right for the node directly to the left of self.
        if col == 0:
            self.left = None
        else:
            self.left = Node.grid[row][col-1]
            Node.grid[row][col-1].right = self
        Node.grid[row].append(self)

    def getPosition(self):
        return [self.row, self.column]

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.xCoord, self.yCoord, self.width, self.height))

main()

#Factors for determining priority:
# 1. Absolute Distance from Node to End
# 2. Shortest found path from Start to current Node
# 3. Absolute Elev change from Node to End

# create a priority list, starting with Start. Look at neighbors.
# if neighbors are a possible move, determine score to rank. 