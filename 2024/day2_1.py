with open('input2.txt', 'r') as file:
    lines = [line.rstrip() for line in file]

#lines = ["7 6 4 2 1", "1 2 7 8 9", "9 7 6 2 1", "1 3 2 4 5", "8 6 4 4 1", "1 3 6 7 9"]

safe_qty = 0
record = []

for line in lines:
    report = [int(i) for i in line.split()]
    report_safe = False
    accepted_changes = []

    print(sorted(report))
    print(sorted(report, reverse=True))

    if report == sorted(report) or report == sorted(report, reverse=True):
        report_safe = True

        for i in range(0, len(report)-1):
            change = report[i] - report[i+1]
            
            if accepted_changes == []:
                if change > 0:
                    accepted_changes = [1,2,3]
                elif change < 0:
                    accepted_changes = [-1,-2,-3]

            if change not in accepted_changes:
                report_safe = False
                break

        accepted_changes = []
    
    if report_safe:
        safe_qty += 1

print(safe_qty)

#352 is too high
            



            
