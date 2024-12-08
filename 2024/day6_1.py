import time

def getInput():
    with open('input6.txt', 'r') as file:
        labMap = [line.rstrip() for line in file]
    
    return labMap
    
def findStart(labMap):
    for rowInd, row in enumerate(labMap):
        for colInd, point in enumerate(row):
            if point == "^":
                startCoord = [rowInd, colInd] 
    return startCoord
    
def moveGuard(currCoord, faceDir, labMap):
    match faceDir:
        case "up":
            moveDir = [-1,0] 
        case "down":
            moveDir = [1,0] 
        case "left":
            moveDir = [0,-1] 
        case "right":
            moveDir = [0,1] 
    
    labMap[currCoord[0]][currCoord[1]] = "X"
    # Element-wise addition
    newCoord = [a + b for a, b in zip(currCoord, moveDir)]
    
    if checkExit(newCoord, len(labMap), len(labMap[0])):
        return newCoord, faceDir, labMap, True
    
    elif labMap[newCoord[0]][newCoord[1]] == "#":
        faceDir = turnGuard(faceDir)
        return currCoord, faceDir, labMap, False
        
    else:
        return newCoord, faceDir, labMap, False
        
    
def checkExit(coord, rows, cols):
    if -1 in coord: #off top or left of map
        return True
    elif len(rows) in coord or len(cols) in coord:
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
            
    reurn faceDir
    
    
if __name__ == "__main__":
    exited = False
    labMap = getInput()
    currCoord = findStart(labMap)
    
    while not exited:
        currCord, faceDir, labMap, exited = moveGuard(currCord, faceDir, labMap)
        print(labMap)
        time.sleep(0.5)
    
    #CountXs()
        
        