def readFile():
    with open("day12sample.txt", "r") as rawHeightMap:
        heightMap = rawHeightMap.readlines()
        for i in range(len(heightMap)):
            heightMap[i] = heightMap[i].strip()
    return heightMap

heightMap = readFile()
print("Heightmap: ", heightMap)