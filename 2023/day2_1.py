class Game:

    def __init__(self, line, **kwargs):
        result_str = line.split(":")[1].split(";")
        
        counts = [ [{color_cnt.split(" ")[2] : int(color_cnt.split(" ")[1])} for color_cnt in round.split(',')] for round in result_str]
        
        self.id = int(line.split("Game ")[1].split(":")[0])
        
        self.possible = True
        for count in counts:
            for item in count:
                color = list(item.keys())[0]
                if item[color] > kwargs['mc'][color]:
                    self.possible = False


if __name__ == "__main__":
    with open('input2_1.txt', 'r') as file:
        lines = [line.rstrip() for line in file]
    
    id_sum = 0
    
    max_colors = {
        'red' : 12,
        'green' : 13,
        'blue' : 14
    }
    
    for line in lines:
        curr_game = Game(line, mc=max_colors)
        if curr_game.possible:
            id_sum += curr_game.id
    
    print(id_sum)