with open('input1.txt', 'r') as file:
    lines = [line.rstrip() for line in file]

#lines = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]

list1, list2 = [], []  

running_total = 0

for line in lines:
    int1, int2 = [int(i) for i in line.split()]
    list1.append(int1)
    list2.append(int2)

list1.sort()
list2.sort()

for a, b in zip(list1, list2):
    running_total += abs(a - b)

print(running_total)