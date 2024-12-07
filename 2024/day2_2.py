def getInput():
    with open('input2.txt', 'r') as file:
        lines = [line.rstrip() for line in file]

    #lines = ["7 6 4 2 1", "1 2 7 8 9", "9 7 6 2 1", "1 3 2 4 5", "8 6 4 4 1", "1 3 6 7 9"]
    return lines

def countSafeReports(lines):
    safe_qty = 0
    for line in lines:
        report = [int(i) for i in line.split()]
        isSafe = testSafety(report)
        if isSafe:
            safe_qty += 1
    return safe_qty
    
def testSafety(report, *args): #pass index to exclude as *args
    isSafe = True
    accepted_changes = []
    
    if args != ():
        removedVal = report[args[0]]
        report.pop(args[0])

    for i in range(len(report)-1):
        change = report[i] - report[i+1]
        
        if accepted_changes == []:
            if change > 0:
                accepted_changes = [1,2,3]
            elif change < 0:
                accepted_changes = [-1,-2,-3]

        if change not in accepted_changes:
            isSafe = False
            if args == ():
                #trigger Problem Dampener once
                for i in range(len(report)):
                    isSafe = testSafety(report, i)
                    if isSafe:
                        break

    if args != ():
        report.insert(args[0], removedVal)
    return isSafe

if __name__ == "__main__":
    lines = getInput()

    print(countSafeReports(lines))
