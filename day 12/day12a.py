import pygame
import math
from queue import PriorityQueue

def readFile():
    with open('day12sample.txt', "r") as rawHeightMap:
        heightMap = rawHeightMap.readlines()
        for i in range(len(heightMap)):
            heightMap[i] = heightMap[i].strip()
    return heightMap

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

class Node:
    _registry = []

    def __init__(self, row, column, elev, start = False, end = False, above = None, below = None, right = None, left = None):
        self.row = row
        self.column = column
        self.elev = elev
        self.start = start
        self.end = end
        self.above = above
        self.below = below
        self.right = right
        self.left = left
        Node._registry[row].append(self)

heightMap = readFile()
nodes = generateNodes(heightMap)

#Factors for determining priority:
# 1. Absolute Distance from Node to End
# 2. Shortest found path from Start to current Node
# 3. Absolute Elev change from Node to End

# create a priority list, starting with Start. Look at neighbors.
# if neighbors are a possible move, determine score to rank. 