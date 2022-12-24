def readFile():
    with open('day3input.txt', 'r') as input:
        rucksacks = input.readlines()
    return rucksacks

def trimRucksacks(rucksacks):
    trimmedRucksacks = []
    for rucksack in rucksacks:
        trimmedRucksacks.append(rucksack.strip())
    return trimmedRucksacks

def getElfGroups(rucksacks):
    elfGroups = []
    numElfs = len(rucksacks)
    elfGroupSize = 3
    for i in range(0, numElfs, elfGroupSize):
        elfGroups.append(rucksacks[i:i+elfGroupSize])
    return elfGroups

def findBadge(elfGroups):
    badges = []
    for group in elfGroups:
        firstElf = set(group[0])
        secondElf = set(group[1])
        thirdElf = set(group[2])
        badges.append(firstElf.intersection(secondElf).intersection(thirdElf)) 
    return badges

totalScore = 0
rucksacks = readFile()
trimmedRucksacks = trimRucksacks(rucksacks)
elfGroups = getElfGroups(trimmedRucksacks)
badges = findBadge(elfGroups)

for badge in badges:
    item = ''.join(str(i) for i in badge)
    if item.isupper():
        score = ord(item)-38
    else:
        score = ord(item)-96
    totalScore += score

print(totalScore)