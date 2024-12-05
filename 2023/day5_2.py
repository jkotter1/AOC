def int_list(int_str):
    return [ int(x) for x  in int_str.strip().split(' ') ]


class mapping:
    def __init__(self, almanac_listing):
        self.range_min = almanac_listing[1]
        self.range_max = almanac_listing[1] + almanac_listing[2]
        self.conversion_val = almanac_listing[0] - almanac_listing[1]


def parse_mappings(lines):
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
    
    return map_list


def map_seed(seed_ranges, section):
    mapped_ranges = []
    for seed_range in seed_ranges:
        for var_map in section:

            if var_map.range_min <= seed_range[0] <= var_map.range_max:
                mapped_ranges.append([x + var_map.conversion_val for x in seed_range])

                if seed_range[1] > var_map.range_max:
                    mapped_ranges[-1][1] = var_map.range_max + var_map.conversion_val
                    new_search_range = [var_map.range_max + 1, seed_range[1]]

                    for x in map_seed([new_search_range], section):
                        mapped_ranges.append(x)

    return mapped_ranges


if __name__ == "__main__":
    with open('2023/test_input5.txt', 'r') as file:
        lines = [line.rstrip() for line in file]

    seeds = int_list(lines[0].split(':')[1])
    seed_ranges = []

    for ind, i in enumerate(seeds[::2]):
        seed_ranges.append([i, i + seeds[2*ind+1] - 1])

    map_list = parse_mappings(lines)
            
    min_location_list = []

    for seed_range in seed_ranges:
        mapped_ranges = []
        mapped_ranges.append(seed_range)

        for section in map_list:
            new_mapped_ranges = map_seed(mapped_ranges, section)
            if len(new_mapped_ranges) != 0:
                mapped_ranges = new_mapped_ranges
        min_location_list.append(min([x[0] for x in mapped_ranges]))        

    print(min(min_location_list))