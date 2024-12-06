def getInput():
    with open('inpu t2.txt', 'r') as file:
        lines = [line.rstrip() for line in file]

    lines = ["7 6 4 2 1", "1 2 7 8 9", "9 7 6 2 1", "1 3 2 4 5", "8 6 4 4 1", "1 3 6 7 9"]
    return lines

safe_qty = 0
record = []

for line in lines:
    report = [int(i) for i in line.split()]
    report_safe = False
    accepted_changes = []

    #if report == sorted(report) or report == sorted(report, reverse=True):
    #    report_safe = True

    for i in range(len(report)-1):
        change = report[i] - report[i+1]
        
        if accepted_changes == []:
            if change > 0:
                accepted_changes = [1,2,3]
            elif change < 0:
                accepted_changes = [-1,-2,-3]

        if change not in accepted_changes:
            #trigger Problem Dampener

    accepted_changes = []
    
    if report_safe:
        safe_qty += 1

print(safe_qty)

if __name__ == "__main__":

            



            
