def getInput():
    with open('input6.txt', 'r') as file:
        labMap = [line.rstrip() for line in file]
    with open('testinput6.txt', 'r') as file:
        labMap = [line.rstrip() for line in file]

    return labMap
    
def findStartAndBlocks(labMap):
    blockCoords = []
    
    for rowInd, row in enumerate(labMap):
        for colInd, point in enumerate(row):
            if point == "^":
                startCoord = [rowInd, colInd]
            elif point == "#":
                blockCoords.append([rowInd, colInd])
    return startCoord, blockCoords
    
def moveGuard(currCoord, faceDir, blockCoords, locLog, labMap, **kwargs):
    match faceDir:
        case "up":
            moveDir = [-1,0] 
        case "down":
            moveDir = [1,0] 
        case "left":
            moveDir = [0,-1] 
        case "right":
            moveDir = [0,1] 
    
    #newRow = list(labMap[currCoord[0]])
    #newRow[currCoord[1]] = "X"
    #labMap[currCoord[0]] = "".join(newRow)

    # Element-wise addition
    newCoord = [a + b for a, b in zip(currCoord, moveDir)]
    
    if checkLoop(newCoord, faceDir, locLog):
        return {newCoord, faceDir, looped := False, exited := True
    
    elif checkExit(newCoord, len(labMap), len(labMap[0])):
        return {newCoord, faceDir, looped := False, exited := True
    
    elif newCoord in blockCoords:
        faceDir = turnGuard(faceDir)
        return {currCoord, faceDir, looped := False, exited := False
        
    else:
        return {newCoord, faceDir, False
        
    
def checkExit(coord, lenRow, lenCol):
    if -1 in coord: #off top or left of map
        return True
    elif lenRow in coord or lenCol in coord:
        return True
    else:
        return False



def turnGuard(faceDir):
    match faceDir:
        case "up":
            faceDir = "right"
        case "down":
            faceDir = "left" 
        case "left":
            faceDir = "up"
        case "right":
            faceDir = "down" 
            
    return faceDir
    
    
    
if __name__ == "__main__":
    exited = False
    labMap = getInput()
    startCoord, blockCoords = findStartAndBlocks(labMap)
    
    
    #getInitialPath
    initialRun = {'currCoord'=startCoord, 'faceDir' = "up", 'blockCoords'=blockCoords, 'locLog'=[], 'labMap'=labMap}
    while not exited:
        initialRun = moveGuard(**initialRun)
        
    print()
        
        