import re

def getInput():
    with open('input3.txt', 'r') as file:
        lines = [line.rstrip() for line in file]

    #lines = ["7 6 4 2 1", "1 2 7 8 9", "9 7 6 2 1", "1 3 2 4 5", "8 6 4 4 1", "1 3 6 7 9"]
    return lines

def getDigits(line):
    line = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    startOfStr = r"^.*?mul\("
    middleOfStr = r"\).*?mul\((?=\d+,\d+\))"
    endOfStr = r"\)(?!mul\(\d+,\d+\))"
    
    pattern = startOfStr +"|"+ middleOfStr +"|"+ endOfStr
    
    print(list(filter(None, re.split(pattern, line[0]))))
    
    return list(filter(None, re.split(pattern, line[0])))
    
def multNums(lines):
    runningTotal = 0
    
    for line in lines:
        nums = getDigits(line)
        for num in nums:
            num1, num2 = [int(i) for i in nums.split(",")]
            runningTotal += num1 * num2
            
    return runningTotal
    
if __name__ == "__main__":
    lines = getInput()
    total = multNums(lines)
    
    print(total)
        