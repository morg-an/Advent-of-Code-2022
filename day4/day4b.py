def readFile():
    with open('input.txt', 'r') as rawData:
        rawData = rawData.readlines()
    return rawData

def getElfSections(itemList):
    pairs = []
    for pair in itemList:
        pair = pair.strip()
        pairs.append(pair.split(','))
    return(pairs)

def getStartEndSections(pairs):
    sections = []
    i = 0
    for pair in pairs:
        sections.append([])
        for elf in pair:
            sections[i].append(elf.split('-'))
        i+= 1
    print(sections)
    return sections

def compare(oneElf, otherElf): #takes 2 ranges
    match = False
    for section in oneElf:
        if section in otherElf:
            match = True
    return match

def compareElfAssignments(sections):
    score = 0
    for pair in sections:

        elf1Start = int(pair[0][0])
        elf1End = int(pair[0][1])
        elf2Start = int(pair[1][0])
        elf2End = int(pair[1][1])

        elf1 = range(elf1Start, elf1End+1)
        elf2 = range(elf2Start, elf2End+1)

        if compare(elf1, elf2) == True or compare(elf2, elf1) == True:
            score += 1

    return score

rawData = readFile()
pairs = getElfSections(rawData)
sections = getStartEndSections(pairs)
score = compareElfAssignments(sections)

print(score)