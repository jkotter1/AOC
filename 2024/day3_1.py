import re

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
        