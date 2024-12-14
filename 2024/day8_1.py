def getInput():
    #with open('input8.txt', 'r') as file:
    #    cityMap = [line.rstrip() for line in file]
    #with open('testinput8.txt', 'r') as file:
    #    cityMap = [line.rstrip() for line in file]

    cityMap = [
        "............",
        "........0...",
        ".....0......",
        ".......0....",
        "....0.......",
        "......A.....",
        "............",
        "............",
        "........A...",
        ".........A..",
        "............",
        "............"
    ]
    
    return cityMap
    
def findAntennas(cityMap):
    antennas = {}
    for rowInd, row in enumerate(cityMap):
        for colInd, point in enumerate(row):
            if point != ".":
                if point in antennas:
                    antennas[point].append((colInd, rowInd))
                else:
                    antennas[point] = [(colInd, rowInd)]
    
    return antennas #list of paired coords as tuples
    
def findAntinodes(antennas):
    nodes=[]
    
    for freq in antennas:
        ants = antennas[freq]
        for antInd, ant in enumerate(ants):
            for i in range(antInd+1, len(ants)):
                nodes += calcAntinodes(ants[antInd], ants[i])

    return nodes

def calcAntinodes(coord1, coord2):
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]

    x3 = x1 - (x2 - x1)
    x4 = x2 + (x2 - x1)

    y3 = y1 - (y2 - y1)
    y4 = y2 + (y2 - y1)
    
    return [(x3,y3), (x4,y4)]

def checkOnMap(coord, cityMap):
    x,y = coord
    
    if x<0 or y<0: #off top or left of map
        return False
    elif x >= len(cityMap[0]) or y >= len(cityMap):
        return False
    else:
        return True
        
    
if __name__ == "__main__":
    locCount = 0
    cityMap = getInput()
    antennas = findAntennas(cityMap)
    nodes = findAntinodes(antennas)
    antinodes = set(nodes)
    
    for node in antinodes:
        if checkOnMap(node, cityMap):
            locCount += 1
    
    print(locCount)
    #returns 17 for test input, should be 14. 