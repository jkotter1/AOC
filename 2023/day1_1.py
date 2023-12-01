with open('C:/Users/jkotter/Documents/GitHub/AOC/2023/input1_1.txt', 'r') as file:
    lines = [line.rstrip() for line in file]

val_sum = 0

for line in lines:

    for char in line:
        if char.isdigit():
            first_digit = char
            break
    
    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break
    
    val_sum += int(first_digit + last_digit)

    print(val_sum)