def getInput():
    with open('input8.txt', 'r') as file:
        cityMap = [line.rstrip() for line in file]
    #with open('testinput8.txt', 'r') as file:
    #    cityMap = [line.rstrip() for line in file]

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
    
def findNodes(antennas, cityMap):
    nodes=[]
    
    for freq in antennas:
        ants = antennas[freq]
        for antInd, ant in enumerate(ants):
            for i in range(antInd+1, len(ants)):
                nodes += calcNodes(ants[antInd], ants[i])

def calcNodes(coord1, coord2):
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]

    slope = (y2 - y1)/(x2 - x1) 
    
    yInt = y1 - slope * x1
    
    distBetween = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    
    distToNode = distBetween / 2
    
    node1x = x1 - distToNode * slope


#old day6_1 code below
def checkExit(coord, lenRow, lenCol):
    if -1 in coord: #off top or left of map
        return True
    elif lenRow in coord or lenCol in coord:
        return True
    else:
        return False
    


    
if __name__ == "__main__":
    exited = False
    labMap = getInput()
    currCoord = findStart(labMap)
    faceDir = "up"
    
    while not exited:
        currCoord, faceDir, labMap, exited = moveGuard(currCoord, faceDir, labMap)
    
    print(countXs(labMap))