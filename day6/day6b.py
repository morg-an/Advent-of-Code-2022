def readFile():
    with open('day6input.txt', 'r') as datastream:
        datastream = datastream.read()
    return datastream

def getSubstrings(datastream):
    i = 13
    lenData = len(datastream)
    substrings = []
    while i < lenData:
        substrings.append(datastream[i-13:i+1])
        i += 1
    return substrings

def findDuplicates(substrings):
    i = 0
    while i < len(substrings):
        unique = True
        for char in substrings[i]:
            compareTo = substrings[i].replace(char, "", 1)
            if char in compareTo:
                unique = False
        if unique == True:
            return i+14 # adding 14 accounts for counting starting at 1 plus 13 for the first thirteen characters before a possible valid marker.
        i += 1
    return "no non-duplicate codes"
    

data = readFile()
substrings = getSubstrings(data)
print(substrings)
print(findDuplicates(substrings))