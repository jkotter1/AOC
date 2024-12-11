import math
from itertools import permutations 

def getInput():
    with open('input7.txt', 'r') as file:
        calib = [line.rstrip() for line in file]
    with open('testinput7.txt', 'r') as file:
        calib = [line.rstrip() for line in file]
    
    cal = {}
    for line in calib:
        nums = line.split(":")[1].split(" ")[1:]
        cal[int(line.split(":")[0])] = [int(i) for i in nums]

    return cal

def tryCalcs(cal):

    for val in cal:
        for ind, i in enumerate(cal[val]):
            ops = ["+"]*ind + ["*"]*(len(cal[val])-1-ind)
            
        if val = math.prod(cal[val]):
            calCount += 1
        
            perm = permutations([1, 2, 3]) 



if __name__ == "__main__":
    calib = getInput()