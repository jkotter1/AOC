class Game:

    def __init__(self, line, **kwargs):
        result_str = line.split(":")[1].split(";")
        results = [ [{color_cnt.split(" ")[2] : int(color_cnt[1])} for color_cnt in round.split(',')] for round in result_str]
        self.id = int(line.split("Game ")[1].split(":")[0])
        self.possible = True

if __name__ == "__main__":
    with open('2023/input2_1.txt', 'r') as file:
        lines = [line.rstrip() for line in file]
    
    id_sum = 0
    max_red = None
    max_green = None
    max_blue = None
    
    for line in lines:
        curr_game = Game(line)
        if curr_game.possible:
            id_sum += curr_game.id