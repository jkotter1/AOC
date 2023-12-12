if __name__ == "__main__":
    with open('2023/input4.txt', 'r') as file:
        lines = [line.rstrip().split(':')[1].split('|') for line in file]
        
        card_val_sum = 0

        for line in lines:
            matches=0
            winners, owned = map(lambda x : x.split(), line)

            winner_ints = {int(x) for x in winners}
            owned_ints = {int(x) for x in owned}
            #print(winner_ints.intersection(owned_ints))
            matches=len(winner_ints.intersection(owned_ints))
            if matches>0:
                card_value = 2 **  (matches-1)
                print(card_value)
                card_val_sum += card_value
        print(card_val_sum)
