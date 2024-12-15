import math
from more_itertools import distinct_permutations as idp

def getInput():
    with open('2024/input7.txt', 'r') as file:
        calib = [line.rstrip() for line in file]
    with open('2024/testinput7.txt', 'r') as file:
       calib = [line.rstrip() for line in file]
    
    calib = ["190: 10 19","3267: 81 40 27","40: 17 5 18","156: 15 6","7290: 6 8 6 15","161011: 16 10 13","192: 17 8 14","21037: 9 7 18 13","292: 11 6 16 20"]
    
    cal = []
    for line in calib:
        testVal = int(line.split(":")[0])
        nums = line.split(":")[1].split(" ")[1:]
        cal += [testVal, [int(i) for i in nums]]

    return cal

def tryCalcs(cal):
    calSum = False

    cc = 0
    for val in cal:
        cc += 1
        print("Calculation " + str(cc) + " of " + str(len(cal)))
        testVal = val[0]
        nums = val[1]
        
        if testVal == math.prod(nums):
                calSum += testVal         
        else:       
            for multInd in enunerate(nums):
                opLog = []
                for concatInd, i in enumerate(nums): #make range dependent on multInd
                    stopCalcs = False
                    
                    ops = ["*"]*multInd + ["||"]*concatInd + ["+"]*(len(nums)-1-multInd-concatInd)
                    opPerms = idp(ops) 
                    
                    for permInd, perm in enumerate(opPerms):
                        if perm in opLog:
                            continue
                        else:
                            opLog.append(perm)
    
                        runningCalc = cal[val][0]
                        
                        for opInd, op in enumerate(perm):
                            if op =="+":
                                runningCalc += nums[opInd+1]
                            elif op == "*":
                                runningCalc *= nums[opInd+1]
                        if runningCalc == val:
                            calSum += val
                            stopCalcs = True
                            break
                
                if stopCalcs:
                    break
    return calSum

if __name__ == "__main__":
    calib = getInput()
    print(tryCalcs(calib))

#20665830406676 is too low