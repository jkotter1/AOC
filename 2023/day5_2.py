def int_list(int_str):
    return [ int(x) for x  in int_str.strip().split(' ') ]

class mapping:
    def __init__(self, almanac_listing):
        self.range_min = almanac_listing[1]
        self.range_max = almanac_listing[1] + almanac_listing[2]
        self.conversion_val = almanac_listing[0] - almanac_listing[1]

class map_range:
    def __init__(self, seed, mapping):
        pass

if __name__ == "__main__":
    with open('2023/input5.txt', 'r') as file:
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
            map_list[map_counter].append(mapping(int_list(line)))
        
    location_list = []


    for seed in seeds:
        #location_val = seed
        for section in map_list:
            for mapping in section:
                if mapping.range_min <= seed <= mapping.range_max:
                    seed += mapping.conversion_val
                    break
        location_list.append(seed)

    print(min(location_list))