def getInput():
    with open('input4.txt', 'r') as file:
        lines = [line.rstrip() for line in file]

    #lines = ["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM", "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"]

    return lines

def checkXmas (lines, lineIndex, charIndex):
    lineCount = 0
    dirsToCheck = []
    dirMods=[-1,0,1]

    for v in dirMods:
        for h in dirMods:
            letter =""
            checkForNeg = [lineIndex + v, lineIndex + v*2, lineIndex + v*3, charIndex + h, charIndex + h*2, charIndex + h*3]
            if min(checkForNeg) >= 0:
                try:
                    letter=lines[lineIndex + v][charIndex + h]
                except IndexError:
                    letter =""
                    
                if letter == "M":
                    dirsToCheck.append([v,h])
                 
    for dir in dirsToCheck:
        try:
            if lines[lineIndex + dir[0]*2][charIndex + dir[1]*2] == "A":
                if lines[lineIndex + dir[0]*3][charIndex + dir[1]*3] == "S":
                    lineCount +=1
        except IndexError:
            pass

    return lineCount
    
def checkForX(lines):
    xmasCnt=0
    
    for lineIndex, line in enumerate(lines):
        for charIndex, letter in enumerate(line):
            if letter == "X":
                xmasCnt += checkXmas(lines, lineIndex, charIndex)
    
    return xmasCnt
                    
if __name__ == "__main__":
    lines = getInput()
    print(checkForX(lines))