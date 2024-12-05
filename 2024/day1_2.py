with open('input1.txt', 'r') as file:
    lines = [line.rstrip() for line in file]

#lines = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]

list1, list2 = [], []  

sim_score = 0

for line in lines:
    int1, int2 = [int(i) for i in line.split()]
    list1.append(int1)
    list2.append(int2)

for num1 in list1:
    for num2 in list2:
        if num1 == num2:
            sim_score += num1

print(sim_score)