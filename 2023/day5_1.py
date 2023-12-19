def int_list(int_str):
    return [ int(x) for x  in int_str.strip().split(' ') ]

if __name__ == "__main__":
    with open('2023/test_input5.txt', 'r') as file:
        lines = [line.rstrip() for line in file]

    seeds = int_list(lines[0].split(':')[1])

    map_counter = -1
    map_list = []

    for line in lines[2:]:
        if ':' in line:
            map_list.append([])
            map_counter += 1
        elif line == '':
            pass
        else:
            map_list[map_counter].append(int_list(line))
        
    print(map_list)