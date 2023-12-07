def is_special_char(char):
    if char.isdigit() or char == '.':
        return False
    else:
        return True
    
'''def is_part_num (lines, row, start_index, end_index):
    
    start_search = max(start_index - 1, 0)
    end_search = min(end_index + 2, len(lines[row]))
    search_lines = [lines[i] for i in range(max(row - 1, 0), min(row + 2, len(lines)))]
    
    search_area = [line[start_search : end_search] for line in search_lines]

    for line in search_area:
        for char in line:
            if is_special_char(char):
                    return True
    
    return False'''

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

    print(num_list)
    '''part_num_sum = 0
    in_num = False
    for row, line in enumerate(lines):
        
        for index, char in enumerate(line):

            if char.isdigit() and not in_num:
                start_ind = index
                in_num = True

            elif in_num and (index == len(line) - 1 or not char.isdigit()):

                if char.isdigit():
                    end_ind = index
                else:
                    end_ind = index - 1

                if is_part_num(lines, row, start_ind, end_ind):
                    print(line[start_ind : end_ind + 1])
                    part_num_sum += int(line[start_ind : end_ind + 1])
                
                in_num = False
    
    print(part_num_sum)'''