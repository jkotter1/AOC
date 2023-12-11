if __name__ == "__main__":
    with open('2023/test_input4.txt', 'r') as file:
        lines = [line.rstrip().split(':')[1].split('|') for line in file]
        
        for line in lines:
            winners, owned = map(lambda x : x.split(), line)

            winner_ints = [int(x) for x in winners]
            owned_ints = [int(x) for x in owned]
            pass
