import re

def getInput():
    with open('input3.txt', 'r') as file:
        lines = [line.rstrip() for line in file]

    #lines = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
    return lines

def getDigits(line):

    startOfStr = r"^.*?mul\("
    middleOfStr = r"\).*?mul\((?=\d+,\d+\))"
    endOfStr = r"\)(?!mul\(\d+,\d+\))"
    
    pattern = startOfStr +"|"+ middleOfStr +"|"+ endOfStr
    
    num_list = list(filter(None, re.split(pattern, line)))
    
    return num_list
    
def multNums(lines):
    runningTotal = 0
    
    for line in lines:
        nums = getDigits(line)
        for num in nums:
            num1, num2 = [int(i) for i in num.split(",")]
            runningTotal += num1 * num2
            
    return runningTotal
    
if __name__ == "__main__":
    lines = getInput()
    total = multNums(lines)
    
    print(total)
        