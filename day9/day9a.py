import math

def readFile():
    with open("day9input.txt", 'r') as fileInput:
        fileInput = fileInput.readlines()
    return fileInput

def parceInput(input):
    parcedInput = []
    for direction in ropeDirections:
        direction = direction.strip('\n').split()
        direction[1] = int(direction[1])
        parcedInput.append(direction)
    return parcedInput

class Rope:
    def __init__(self, xHead = 0, yHead = 0, xTail = 0, yTail = 0, tailPath=[[0,0]]):
        self.xHead = xHead
        self.yHead = yHead
        self.xTail = xTail
        self.yTail = yTail
        self.tailPath = tailPath
    
    def printRopeDetails(self):
        print(f"Head at row {self.yHead}, column {self.xHead}.")
        print(f"Tail at row {self.yTail}, column {self.xTail}.")
    
    def getXHead(self):
        return self.xHead

    def getYHead(self):
        return self.yHead
    
    def getXTail(self):
        return self.xTail

    def getYTail(self):
        return self.yTail

    def moveHead(self, instructions):
        print(instructions)
        moveDirection = instructions[0]
        moveDistance = instructions[1]
        if moveDirection == 'U':
            self.yHead += moveDistance
        if moveDirection == 'D':
            self.yHead -= moveDistance
        if moveDirection == 'R':
            self.xHead += moveDistance
        if moveDirection == 'L':
            self.xHead -= moveDistance
        print(f"Head at row {self.yHead}, column {self.xHead}.")
    
    def moveTail(self, instructions):
        #find difference
        xDifference = self.xTail - self.xHead
        yDifference = self.yTail - self.yHead
        print(f"xDifference: {xDifference}   yDifference: {yDifference}")
        if abs(xDifference) > 1 or abs(yDifference) > 1:
            i = 0
            if yDifference == 0:
                if xDifference < 0: #move right
                    numMoves = (xDifference*-1)-1
                    self.xTail += numMoves
                    while i < numMoves:
                        pathStop = [self.xTail-i, self.yTail]
                        if pathStop not in self.tailPath:
                            self.tailPath.append(pathStop)
                        i += 1
                else: #move left
                    numMoves = xDifference-1
                    self.xTail -= numMoves
                    while i < numMoves:
                        pathStop = [self.xTail+i, self.yTail]
                        if pathStop not in self.tailPath:
                            self.tailPath.append(pathStop)
                        i += 1
            elif xDifference == 0:
                if yDifference < 0: #move up
                    numMoves = (yDifference*-1)-1
                    self.yTail += numMoves
                    while i < numMoves:
                        pathStop = [self.xTail, self.yTail-i]
                        if pathStop not in self.tailPath:
                            self.tailPath.append(pathStop)
                        i += 1
                else: # move down
                    numMoves = yDifference-1
                    self.yTail -= numMoves
                    while i < numMoves:
                        pathStop = [self.xTail, self.yTail+i]
                        if pathStop not in self.tailPath:
                            self.tailPath.append(pathStop)
                        i += 1
            # move if x and y are both different
            else:
                moveDirection = instructions[0]
                numMovesUp = numMovesDown = numMovesLeft = numMovesRight = None
                j = 0

                if moveDirection == 'U':
                    numMovesUp = abs(yDifference)-2
                    if xDifference > 0: #left
                        numMovesLeft = xDifference
                        while j < numMovesLeft:
                            pathStop = [self.xTail-1, self.yTail+1]
                            if pathStop not in self.tailPath:
                                self.tailPath.append(pathStop)
                            j += 1
                    if xDifference < 0: #right
                        numMovesRight = abs(xDifference)
                        while j < numMovesRight:
                            pathStop = [self.xTail+1, self.yTail+1]
                            if pathStop not in self.tailPath:
                                self.tailPath.append(pathStop)
                            j += 1
                    self.xTail = self.xHead
                    self.yTail = self.yHead-1
                    while i < numMovesUp:
                        pathStop = [self.xTail, self.yTail-i]
                        if pathStop not in self.tailPath:
                            self.tailPath.append(pathStop)
                        i += 1

                elif moveDirection == 'R':
                    numMovesRight = abs(xDifference)-2
                    if yDifference > 0: #down
                        numMovesDown = yDifference
                        while j < numMovesDown:
                            pathStop = [self.xTail+1, self.yTail-1]
                            if pathStop not in self.tailPath:
                                self.tailPath.append(pathStop)
                            j += 1
                    if yDifference < 0: #up
                        numMovesUp = abs(yDifference)
                        while j < numMovesUp:
                            pathStop = [self.xTail+1, self.yTail+1]
                            if pathStop not in self.tailPath:
                                self.tailPath.append(pathStop)
                            j += 1
                    self.yTail = self.yHead
                    self.xTail = self.xHead-1
                    while i < numMovesRight:
                        pathStop = [self.xTail-i, self.yTail]
                        if pathStop not in self.tailPath:
                            self.tailPath.append(pathStop)
                        i += 1

                elif moveDirection == 'D':
                    numMovesDown = yDifference -2
                    if xDifference > 0: #left
                        numMovesLeft = xDifference
                        while j < numMovesLeft:
                            pathStop = [self.xTail-1, self.yTail-1]
                            if pathStop not in self.tailPath:
                                self.tailPath.append(pathStop)
                            j += 1
                    if xDifference < 0: #right
                        numMovesRight = abs(xDifference)
                        while j < numMovesRight:
                            pathStop = [self.xTail+1, self.yTail-1]
                            if pathStop not in self.tailPath:
                                self.tailPath.append(pathStop)
                            j += 1
                    self.xTail = self.xHead
                    self.yTail = self.yHead+1
                    while i < numMovesDown:
                        pathStop = [self.xTail, self.yTail+i]
                        if pathStop not in self.tailPath:
                            self.tailPath.append(pathStop)
                        i += 1   

                elif moveDirection == 'L':
                    numMovesLeft = xDifference -2
                    if yDifference > 0: #down
                        numMovesDown = yDifference
                        while j < numMovesDown:
                            pathStop = [self.xTail-1, self.yTail-1]
                            if pathStop not in self.tailPath:
                                self.tailPath.append(pathStop)
                            j += 1
                    if yDifference < 0: #up
                        numMovesUp = abs(yDifference)
                        while j < numMovesUp:
                            pathStop = [self.xTail-1, self.yTail+1]
                            if pathStop not in self.tailPath:
                                self.tailPath.append(pathStop)
                            j += 1
                    self.yTail = self.yHead
                    self.xTail = self.xHead+1
                    while i < numMovesLeft:
                        pathStop = [self.xTail+i, self.yTail]
                        if pathStop not in self.tailPath:
                            self.tailPath.append(pathStop)
                        i += 1


                print(f"Num Moves - Up: {numMovesUp} Down: {numMovesDown} Right: {numMovesRight} Left: {numMovesLeft}")

                if xDifference < 0 and yDifference < 0: # Up & Right - append tailpath
                    pass
                elif xDifference > 0 and yDifference > 0: # Down & Left - append tailpath
                    pass
                elif xDifference > 0 and yDifference < 0: # Up & Left - append tailpath
                    pass
                elif xDifference < 0 and yDifference > 0: # Down & Right - append tailpath
                    pass

        print(f"Tail at row {self.yTail}, column {self.xTail}.")
        print(f"Tail Path: {self.tailPath}\n")
        print(len(self.tailPath))

def moveString(rope, parcedInput):
    for line in parcedInput:
        rope.moveHead(line)
        rope.moveTail(line)

ropeDirections = readFile()
parcedInput = parceInput(ropeDirections)
rope = Rope()
moveString(rope, parcedInput)