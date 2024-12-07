def getInput():
    with open('input4.txt', 'r') as file:
        lines = [line.rstrip() for line in file]

    return lines

def checkXmas (lines, lineIndex, charIndex)
    dirMods=[-1,0,1]

    for v in dirMods:
        for h in dirMods:
            letter =""
            
            try:
                letter=lines[lineIndex + v][charIndex + h]
            except IndexError:
                letter =""
                
            if letter == "M":
                dirsToCheck.append([v,h])
                 
    for dir in dirsToCheck:
        try:
            if lines[dir[0]*2][dir[1]*2] == "A":
                if lines[dir[0]*3][dir[1]*3] == "S":
                    xmasCnt +=1
         except IndexError:
            
    return xmasCnt
    
def checkForX(lines):
    xmasCnt=0
    
    for lineIndex, line in lines:
        for charIndex, letter in line:
            if letter == "X":
                xmasCnt += checkXmas(lines, lineIndex, charIndex)
    
    return xmasCnt
                    
if __name__ == "__main__":
    lines = getInput()
    print(checkForX(lines))