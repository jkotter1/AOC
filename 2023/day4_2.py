if __name__ == "__main__":
    with open('2023/input4.txt', 'r') as file:
        lines = [line.rstrip().split(':')[1].split('|') for line in file]
        
        card_sum = 0

        num_copies = [1 for i in range(len(lines))]

        for index, line in enumerate(lines):
            matches=0
            winners, owned = map(lambda x : x.split(), line)

            winner_ints = {int(x) for x in winners}
            owned_ints = {int(x) for x in owned}

            matches=len(winner_ints.intersection(owned_ints))
            for match in range(1,matches + 1):
                num_copies[index + match] += 1 * num_copies[index]

        print(sum(num_copies))
