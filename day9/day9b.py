def readFile():
    with open("day9input.txt", 'r') as fileInput:
        fileInput = fileInput.readlines()
        print(fileInput)
    return fileInput

def parceInput(directions):
    parcedInput = []
    for direction in directions:
        direction = direction.strip('\n').split()
        direction[1] = int(direction[1])
        parcedInput.append(direction)
    return parcedInput

class Rope:
    def __init__(self, length = 10, tailPath=[(0,0)], tautSegments = 0):
        # head & Tail = [horizontal/column/x, vertical/row/y]
        self.length = length
        self.position = []
        i = 0
        while i < length:
            self.position.append([0,0])
            i += 1
        self.head = self.position[0]
        self.tail = self.position[-1]
        self.tailPath = tailPath
        self.tautSegments = 0

    def printRopeDetails(self):
        print(f"Head:   {self.position[0]}")
        i = 1
        while i < self.length-1:
            print(f"Knot {i}: {self.position[i]}")
            i += 1
        print(f"Tail:   {self.position[-1]} \n")

    def moveHead(self, instruction):
        moveDirection = instruction[0]
        head = self.position[0]
        if moveDirection == 'U':
            head[1] += 1
        if moveDirection == 'D':
            head[1] -= 1
        if moveDirection == 'R':
            head[0] += 1
        if moveDirection == 'L':
            head[0] -= 1
        #print(f"Moved 1 {moveDirection}: Head now at row {self.head[1]}, column {self.head[0]}.")

    def appendTailPath(self):
        tailLocation = (self.position[-1][0], self.position[-1][1])
        if tailLocation not in self.tailPath:
            self.tailPath.append(tailLocation)
        print(f"Appended to Path: {tailLocation} \n")

    def moveUp(self, knot):
        self.position[knot][1] += 1

    def moveDown(self, knot):
        self.position[knot][1] -= 1

    def moveLeft(self, knot):
        self.position[knot][0] -= 1

    def moveRight(self, knot):
        self.position[knot][0] += 1

    def tailFollows(self, instruction):
        knot = 1
        while knot < self.length:
            horDiff = self.position[knot][0] - self.position[knot-1][0]
            vertDiff = self.position[knot][1] - self.position[knot-1][1]

            # Straight Lines
            if vertDiff == 0 and horDiff == -2:
                self.moveRight(knot)
            elif vertDiff == 0 and horDiff == 2:
                self.moveLeft(knot)
            elif horDiff == 0 and vertDiff == -2:
                self.moveUp(knot)
            elif horDiff == 0 and vertDiff == 2:
                self.moveDown(knot)

            # Diagonal Moves
            elif (vertDiff == -2 and horDiff == -1) or (vertDiff == -1 and horDiff == -2) or (vertDiff == -2 and horDiff == -2):
                self.moveUp(knot)
                self.moveRight(knot)
            elif (vertDiff == -2 and horDiff == 1) or (vertDiff == -1 and horDiff == 2) or (vertDiff == -2 and horDiff == 2):
                self.moveUp(knot)
                self.moveLeft(knot)
            elif (vertDiff == 2 and horDiff == -1) or (vertDiff == 1 and horDiff == -2) or (vertDiff == 2 and horDiff == -2):
                self.moveDown(knot)
                self.moveRight(knot)
            elif (vertDiff == 2 and horDiff == 1) or (vertDiff == 1 and horDiff == 2) or (vertDiff == 2 and horDiff == 2):
                self.moveDown(knot)
                self.moveLeft(knot)

            self.appendTailPath()

            knot += 1

    def move(self, instructions):
        for instruction in instructions:
            print(instruction)
            numMoves = instruction[1]
            i = 0
            while i < numMoves:
                self.moveHead(instruction)
                self.tailFollows(instruction)
                print("mid-move: ", self.position)
                i += 1
            print('\n')

ropeInstructions = readFile()
parcedInput = parceInput(ropeInstructions)
rope = Rope()
rope.move(parcedInput)
print(rope.tailPath)
print(len(rope.tailPath))