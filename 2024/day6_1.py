def getInput():
    with open('input5a.txt', 'r') as file:
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
    checkExit(newCoord)
    
def checkExit(coord):
    if (-1 in coord) 
    
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
    print(logMidVals(getInput()))