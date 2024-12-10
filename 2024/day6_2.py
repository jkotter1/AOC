def getInput():
    with open('input6.txt', 'r') as file:
        labMap = [line.rstrip() for line in file]
    #with open('testinput6.txt', 'r') as file:
    #    labMap = [line.rstrip() for line in file]
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

def moveGuard(**kwargs):
    currCoord = kwargs.get('currCoord')
    faceDir = kwargs.get('faceDir')
    blockCoords = kwargs.get('blockCoords')
    locLog = kwargs.get('locLog')
    labMap = kwargs.get('labMap')

    moveDir = [None]
    match faceDir:
        case "up":
            moveDir = [-1,0] 
        case "down":
            moveDir = [1,0] 
        case "left":
            moveDir = [0,-1] 
        case "right":
            moveDir = [0,1] 

    # Change guard coordinate
    newCoord = [a + b for a, b in zip(currCoord, moveDir)]
    if newCoord in blockCoords: #if guard hits block, turn and don't progress
        faceDir = turnGuard(faceDir)
        newCoord = currCoord

    if [newCoord, faceDir] in locLog: #if guard has been at this coord facing the same direction, guard has looped
        return {'looped': True, 'exited': True}
    
    elif checkExit(newCoord, len(labMap), len(labMap[0])):
        return {'looped': False, 'exited': True, 'locLog':locLog}
    
    else:
        locLog.append([newCoord, faceDir])
    
    return {'currCoord': newCoord, 'faceDir': faceDir, 'blockCoords': blockCoords, 'locLog': locLog, 'labMap': labMap, 'looped': False, 'exited': False}


if __name__ == "__main__":
    exited = False
    looped = False
    labMap = getInput()
    startCoord, blockCoords = findStartAndBlocks(labMap)

    #getInitialPath
    initialRun = {'currCoord':startCoord, 'faceDir': "up", 'blockCoords':blockCoords, 'locLog':[], 'labMap':labMap}
    while not exited:
        initialRun = moveGuard(**initialRun)
        exited = initialRun['exited']
        
    #print(initialRun['locLog'])
    possibleNewBlocks = initialRun['locLog']
    newBlockLog = []

    for ind, newBlock in enumerate(possibleNewBlocks):
        print("Testing Block " + str(ind) + " of " + str(len(possibleNewBlocks)))
        exited = False
        looped = False
        newBlockCoords = blockCoords + [newBlock[0]]  
        currRun = {'currCoord':startCoord, 'faceDir': "up", 'blockCoords':newBlockCoords, 'locLog':[], 'labMap':labMap}

        while not exited:
            currRun = moveGuard(**currRun)
            exited = currRun['exited']
            if currRun['looped']:
                newBlockLog.append(newBlock[0])
    
    newBlockLocs = []
    for blockLoc in newBlockLog:
        if blockLoc not in newBlockLocs:
            newBlockLocs.append(blockLoc)
    
    print(len(newBlockLocs))