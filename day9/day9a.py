def readFile():
    with open("day9sample.txt", 'r') as fileInput:
        fileInput = fileInput.readlines()
    return fileInput

def parceInput(directions):
    parcedInput = []
    for direction in directions:
        direction = direction.strip('\n').split()
        direction[1] = int(direction[1])
        parcedInput.append(direction)
    return parcedInput

class Rope:
    def __init__(self, length = 1, head = [0, 0], tail = [0, 0], tailPath=[(0,0)]):
        # head & Tail = [horizontal/column/x, vertical/row/y]
        self.length = length
        self.head = head
        self.tail = tail
        self.tailPath = tailPath

    def printRopeDetails(self):
        print(f"Rope Length: {self.length}")
        print(f"Head at row {self.head[1]}, column {self.head[0]}.")
        print(f"Tail at row {self.tail[1]}, column {self.tail[0]}.'\n")

    def moveHead(self, instruction):
        moveDirection = instruction[0]
        if moveDirection == 'U':
            self.head[1] += 1
        if moveDirection == 'D':
            self.head[1] -= 1
        if moveDirection == 'R':
            self.head[0] += 1
        if moveDirection == 'L':
            self.head[0] -= 1
        #print(f"Moved 1 {moveDirection}: Head now at row {self.head[1]}, column {self.head[0]}.")

    def moveTailHorizontal(self, horizontalDiff):
        if horizontalDiff < 0:
            self.tail[0] += 1
        else:
            self.tail[0] -= 1
    
    def moveTailVertical(self, verticalDiff):
        if verticalDiff < 0:
            self.tail[1] += 1
        else:
            self.tail[1] -= 1

    def appendPath(self):
        tailLocation = self.tail[0], self.tail[1]
        headLocation = self.head[0], self.head[1]
        if tailLocation not in self.tailPath:
            self.tailPath.append(tailLocation)
        print(f"Appended to Path: {self.tailPath} \n")

    def tailFollows(self, instruction):
        lastMoveDirection = instruction[0]
        horizontalDiff = self.tail[0] - self.head[0]
        verticalDiff = self.tail[1] - self.head[1]
        #print(f"Row Diff: {horizontalDiff}, Column Diff: {verticalDiff}")
        if abs(horizontalDiff) <= self.length and abs(verticalDiff) <= self.length:
            return

        # if only one axis is different
        if verticalDiff == 0 and horizontalDiff < 0: #move right
            self.tail[0] += 1
        elif verticalDiff == 0 and horizontalDiff > 0: #move left
            self.tail[0] -= 1
        elif horizontalDiff == 0 and verticalDiff < 0: #move up
            self.tail[1] += 1
        elif horizontalDiff == 0 and verticalDiff > 0: #move down
            self.tail[1] -= 1

        # if both axis are different
        else:
            if lastMoveDirection == 'U':
                self.tail[1] += 1
                self.moveTailHorizontal(horizontalDiff)
            elif lastMoveDirection == 'D':
                self.tail[1] -= 1
                self.moveTailHorizontal(horizontalDiff)
            elif lastMoveDirection == 'R':
                self.tail[0] += 1
                self.moveTailVertical(verticalDiff)
            elif lastMoveDirection == 'L':
                self.tail[0] -= 1
                self.moveTailVertical(verticalDiff)
        self.appendPath()

    def move(self, instructions):
        for instruction in instructions:
            print(instruction)
            numMoves = instruction[1]
            i = 0
            while i < numMoves:
                self.moveHead(instruction)
                self.tailFollows(instruction)
                i += 1
            print(f"Head: {self.head} Tail: {self.tail}")
        print(f"Tail Path: {self.tailPath} (len = {len(self.tailPath)})\n")

ropeInstructions = readFile()
parcedInput = parceInput(ropeInstructions)
rope = Rope()
rope.move(parcedInput)