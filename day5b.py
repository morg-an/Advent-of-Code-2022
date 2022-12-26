import math

def readFile():
    with open('day5input.txt', 'r') as rawData:
        rawData = rawData.read()
    return rawData

def getRawStack(data):
    dataList = data.split('\n\n')
    return dataList[0]

def getNumPiles(stack):
    piles = stack.split('   ')
    numPiles = int(piles[-1])
    return numPiles

def getMoves(data):
    dataList = data.split('\n\n')
    moves = dataList[1].split('\n')
    moveArray = []

    for move in moves:
        moveDetails = move.split(" ")
        numMoves = int(moveDetails[1])
        moveStart = int(moveDetails[3])
        moveEnd = int(moveDetails[5])
        moveArray.append([numMoves, moveStart, moveEnd])
    
    return moveArray

def createStackDict(stack, numPiles):
    stack = stack.split('\n')
    stack.pop()
    stackDict = {}

    for num in range(numPiles):
        stackDict[num+1] = []

    for row in reversed(stack):
        i = 0
        for char in row:
            if char == "":
                i += 1
            elif char == '[':
                i += 1
            elif char == ']':
                i += 1
            elif char == " ":
                i += 1
            else:
                charIndex = i
                stackNum = math.ceil(charIndex/4)
                stackDict[stackNum].append(char)
                i += 1
    return stackDict

def executeMoves(stackDict, moves):
    print("StackDict: ", stackDict)
    for move in moves:
        print("Move: ", move)
        nextChars = []
        for num in range(move[0]):
            nextChar = stackDict[move[1]].pop()
            nextChars.insert(0, nextChar)
        print("Next to Move: ", nextChars)
        stackDict[move[2]] += nextChars
        print("New StackDict: ", stackDict)
    return stackDict

def getAnswer(stackDict):
    answer = ""
    for i in range(numPiles):
        answer += stackDict[i+1][-1]
    return answer

data = readFile()
rawStack = getRawStack(data)
moves = getMoves(data)
numPiles = getNumPiles(rawStack)
stackDict = createStackDict(rawStack, numPiles)
stackDict = executeMoves(stackDict, moves)
answer = getAnswer(stackDict)

print(answer)