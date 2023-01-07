import pygame
import math
from queue import PriorityQueue

colors = {'white':('#ffffff', 5), 'gray1':('#f0f0f0', 6), 'gray2':('#d4d4d4', 17),
'gray3':('#b8b8b8', 28), 'gray4':('#9c9c9c', 39), 'gray5':('#7f7f7f', 50),
'gray6':('#636363', 61), 'gray7':('#474747', 72), 'gray8':('#2b2b2b', 83),
'gray9':('#0f0f0f', 94), 'black':('#000000', 100)}

def readFile():
    with open('day12sample.txt', "r") as rawHeightMap:
        heightMap = rawHeightMap.readlines()
        for i in range(len(heightMap)):
            heightMap[i] = heightMap[i].strip()
    return heightMap

def drawDisplay(heightMap):
    height = len(heightMap) * 100
    width = len(heightMap[0]) * 100
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Hill Climbing Algorithm")

def generateNodes(heightMap):
    for i in range(len(heightMap)): #iterate rows - bottom to top
        row = heightMap[(i + 1)*-1]
        Node._registry.append([])
        for j in range(len(row)): #iterate columns - left to right
            node = Node(i, j, row[j])
            if j == 'S':
                node.start = True
                node.elev = 'a'
            if j == 'E':
                node.end = True
                node.elev = 'z'

def mapAdjacentNodes():
    #write a function to relate each node above, below, and to each side
    pass

def estimateDistance(p1, p2):
    #stimate the distance between two points
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)
    pass

class Node:
    _registry = []

    def __init__(self, row, col, elev, width = 100, start = False, end = False, above = None, below = None, right = None, left = None):
        self.row = row
        self.col = col
        self.elev = elev
        self.width = width
        self.xCoord = row * width
        self.yCoord = col * width
        self.color = colors['white']
        self.start = start
        self.end = end
        self.above = above
        self.below = below
        self.right = right
        self.left = left
        Node._registry[row].append(self)

    def getPosition(self):
        return [self.row, self.column]

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.xCoord, self.yCoord, self.width, self.width))

heightMap = readFile()
drawDisplay(heightMap)
nodes = generateNodes(heightMap)

#Factors for determining priority:
# 1. Absolute Distance from Node to End
# 2. Shortest found path from Start to current Node
# 3. Absolute Elev change from Node to End

# create a priority list, starting with Start. Look at neighbors.
# if neighbors are a possible move, determine score to rank. 