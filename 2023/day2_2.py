class Game:

    def __init__(self, line, **kwargs):
        result_str = line.split(":")[1].split(";")
        
        counts = [ [{color_cnt.split(" ")[2] : int(color_cnt.split(" ")[1])} for color_cnt in round.split(',')] for round in result_str]
        
        self.id = int(line.split("Game ")[1].split(":")[0])
        
        for count in counts:
            for item in count:
                color = list(item.keys())[0]
                if item[color] > kwargs['mc'][color]:
                    kwargs['mc'][color] = item[color]

        self.power = 1
        for x in list(kwargs['mc'].values()):
            self.power = self.power * x 
        #print(self.power)

        for color in list(kwargs['mc'].keys()):
            kwargs['mc'][color] = 0 


if __name__ == "__main__":
    with open('input2_1.txt', 'r') as file:
        lines = [line.rstrip() for line in file]
    
    power_sum = 0
    
    max_colors = {
        'red' : 0,
        'green' : 0,
        'blue' : 0
    }
    
    for line in lines:
        power_sum += Game(line, mc=max_colors).power
         
    print(power_sum)