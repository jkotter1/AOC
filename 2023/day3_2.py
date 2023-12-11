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

class SearchArea:
    def __init__(self, lines, gear_line, gear_index):
        self.search_lines = [ i for i in range( max(0, gear_line - 1), min(len(lines), gear_line + 2) ) ]
        self.search_indices = [ i for i in range( max (0, gear_index - 1), min(len(lines[0]), gear_index + 2) ) ]

if __name__ == "__main__":
    with open('2023/input3_1.txt', 'r') as file:
        lines = [line.rstrip() for line in file]

    num_list = find_nums(lines)
    gear_ratio_sum = 0

    for line_index, line in enumerate(lines):
        #gear_count = 0
        for char_index, char in enumerate(line):
            if char == '*':
                curr_search = SearchArea(lines, line_index, char_index)

                adjacent_nums = []

                for search_line in curr_search.search_lines:
                    for search_index in curr_search.search_indices:
                        for num in num_list[search_line]:
                            if search_index in num:
                                if [search_line, num] not in adjacent_nums:
                                    adjacent_nums.append([search_line, num])

                if len(adjacent_nums) == 2:
                    gear_ratio = 1
                    for adj_num in adjacent_nums:
                        gear_num = int(''.join(lines[adj_num[0]][i] for i in range(adj_num[1][0],adj_num[1][1]+1)))
                        gear_ratio *= gear_num 
                    print(gear_ratio)
                    gear_ratio_sum += gear_ratio

    [print(gear_ratio_sum)]
