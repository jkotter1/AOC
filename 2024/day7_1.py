import math
from itertools import permutations 

def getInput():
    with open('input7.txt', 'r') as file:
        calib = [line.rstrip() for line in file]
    with open('testinput7.txt', 'r') as file:
        calib = [line.rstrip() for line in file]
    
    calib = ["190: 10 19","3267: 81 40 27","83: 17 5","156: 15 6","7290: 6 8 6 15","161011: 16 10 13","192: 17 8 14","21037: 9 7 18 13","292: 11 6 16 20"]
    
    cal = {}
    for line in calib:
        nums = line.split(":")[1].split(" ")[1:]
        cal[int(line.split(":")[0])] = [int(i) for i in nums]

    return cal

def tryCalcs(cal):
    calCount = 0
    
    for val in cal:
        runningCalc = 0
        if val = math.prod(cal[val]):
                calCount += 1
                break
                
        for ind, i in enumerate(cal[val]):
            ops = ["+"]*ind + ["*"]*(len(cal[val])-1-ind)
            
            
            else:
                opPerms = permutations(ops) 
                for permInd, perm in enumerate(opPerms):
                    for op in perm:
                        if op =="+":
                            


if __name__ == "__main__":
    calib = getInput()