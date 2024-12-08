def getInput():
    with open('input4.txt', 'r') as file:
        lines = [line.rstrip() for line in file]

    #lines = ["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM", "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"]

    return lines

def checkXmas (lines, lineIndex, charIndex):
    isXmas = 0
    
    upLeft = lines[lineIndex-1][charIndex-1]
    upRight = lines[lineIndex-1][charIndex+1]
    downLeft = lines[lineIndex+1][charIndex-1]
    downRight = lines[lineIndex+1][charIndex+1]

    if (upLeft == "S" and downRight == "M") or (upLeft == "M" and downRight == "S"):
        if (upRight == "S" and downLeft == "M") or (upRight == "M" and downLeft == "S"):
            isXmas=1

    return isXmas
    
def checkForA(lines):
    xmasCnt=0
    
    for lineIndex, line in enumerate(lines):
        for charIndex, letter in enumerate(line):
            if letter == "A" and lineIndex not in [0, len(lines)-1] and charIndex not in [0, len(line)-1]:
                xmasCnt += checkXmas(lines, lineIndex, charIndex)
    
    return xmasCnt
                    
if __name__ == "__main__":
    lines = getInput()
    print(checkForA(lines))