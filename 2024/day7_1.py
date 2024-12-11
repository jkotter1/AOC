import math
from more_itertools import distinct_permutations as idp

def getInput():
    with open('input7.txt', 'r') as file:
        calib = [line.rstrip() for line in file]
    with open('testinput7.txt', 'r') as file:
       calib = [line.rstrip() for line in file]
    
    #calib = ["190: 10 19","3267: 81 40 27","83: 17 5","156: 15 6","7290: 6 8 6 15","161011: 16 10 13","192: 17 8 14","21037: 9 7 18 13","292: 11 6 16 20"]
    
    cal = {}
    for line in calib:
        nums = line.split(":")[1].split(" ")[1:]
        cal[int(line.split(":")[0])] = [int(i) for i in nums]

    return cal

def tryCalcs(cal):
    calSum = False

    
    for val in cal:
        cc = 1
        print("Calculation "+str(cc)+" of "+str(len(cal)))
        nums = cal[val]
        if val == math.prod(nums):
                calSum += val
                
        else:       
            for ind, i in enumerate(nums):
                opLog = []
                stopCalcs = False
                ops = ["*"]*ind + ["+"]*(len(nums)-1-ind)
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