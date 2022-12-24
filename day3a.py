def readFile():
    with open('day3input.txt', 'r') as input:
        rucksacks = input.readlines()
    return rucksacks

def getCompartments(allContents):
    rucksackContents = []
    totalSize = int(len(allContents.strip()))
    compartmentSize = int(totalSize/2)

    rucksackContents.append(allContents[slice(compartmentSize)])
    rucksackContents.append(allContents[slice(compartmentSize, totalSize)])

    return rucksackContents

def findMisplacedItem(rucksack):
    firstCompartment = set(rucksack[0])
    secondCompartment = set(rucksack[1])
    misplacedItem = firstCompartment.intersection(secondCompartment)
    return misplacedItem

rucksacks = readFile()
totalScore = 0

for rucksack in rucksacks:
    compartments = getCompartments(rucksack)
    misplacedItem = findMisplacedItem(compartments)
    item = ''.join(str(i) for i in misplacedItem)
    if item.isupper():
        score = ord(item)-38
    else:
        score = ord(item)-96
    totalScore += score

print(totalScore)