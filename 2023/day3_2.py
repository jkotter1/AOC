def find_nums(lines): #Returns a list for each line of the file with [start_index, end_index] lists for the locations of every distinct number (i.e. run of digits) 
    
    nums_by_line = []
    in_num = False

    for line_index, line in enumerate(lines):
        num_count = 0
        nums_by_line.append([])

        for index, char in enumerate(line):
            
            if index == 0 and in_num:
                nums_by_line[line_index - 1][-1][1] = len(line) - 1  
                in_num = False #If the last line ended in a number, reset the indicator at the start of the new line 

            if char.isdigit():
                if not in_num:
                    nums_by_line[line_index].append([index, None]) #if not in a number already, append a list of [first,last] indices for a new number
                    in_num = True
            else:
                if in_num:
                    nums_by_line[line_index][num_count][1] = index - 1
                    in_num = False
                    num_count += 1
    
    if nums_by_line[-1][-1][1] == None:
        nums_by_line[-1][-1][1] = len(lines[-1]) - 1

    return nums_by_line

if __name__ == "__main__":
    with open('2023/test_input3_1.txt', 'r') as file:
        lines = [line.rstrip() for line in file]

    num_list = find_nums(lines)

    for line in lines:
        gear_count = 0
        for char in line:
            if char == '*':
                gear_count +=1
        print(gear_count)

