import re

def getInput():
    with open('input3.txt', 'r') as file:
        lines = [line.rstrip() for line in file]

        concatLines = "".join(([x for line in lines for x in line]))

    #concatLines = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    return concatLines

def purgeDonts(line):
    dontPattern = r"don't\(\).*?do\(\)"
    doList = re.split(dontPattern, line)
    doLine = "".join(doList)

    return doLine

def getDigits(line):

    startOfStr = r"^.*?mul\("
    middleOfStr = r"\).*?mul\((?=\d+,\d+\))"
    endOfStr = r"\)(?!mul\(\d+,\d+\))"
    
    pattern = startOfStr +"|"+ middleOfStr +"|"+ endOfStr
    
    num_list = list(filter(None, re.split(pattern, line)))
    
    return num_list
    
def multNums(line):
    runningTotal = 0
    
    nums = getDigits(line)
    for num in nums:
        num1, num2 = [int(i) for i in num.split(",")]
        runningTotal += num1 * num2
            
    return runningTotal
    
if __name__ == "__main__":
    line = getInput()
    doLine = purgeDonts(line)
    total = multNums(doLine)
    
    print(total)
        