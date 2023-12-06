def is_special_char(char):
    if char.isdigit() or char == '.':
        return False
    else:
        return True
    
def is_part_num (lines, row, start_index, end_index):
    
    start_search = max(start_index - 1, 0)
    end_search = min(end_index + 2, len(lines[row]) - 1)
    search_lines = [lines[i] for i in range(max(row - 1, 0), min(row + 2, len(lines) - 1))]
    
    search_area = [line[start_search : end_search] for line in search_lines]

    part_num = False

    for line in search_area:
        for char in line:
            if is_special_char(char):
                part_num = True
    
    return part_num

if __name__ == "__main__":
    with open('2023/input3_1.txt', 'r') as file:
        lines = [line.rstrip() for line in file]

    part_num_sum = 0

    for row, line in enumerate(lines):
        in_num = False
        for index, char in enumerate(line):

            if char.isdigit() and not in_num:
                start_ind = index
                in_num = True

            elif in_num and not char.isdigit():
                
                if is_part_num(lines, row, start_ind, index-1):
                    print(line[start_ind : index])
                    part_num_sum += int(line[start_ind : index])
                
                in_num = False
    
    print(part_num_sum)