def getInput():
    with open('input5a.txt', 'r') as file:
        rules = [line.rstrip() for line in file]
    with open('input5b.txt', 'r') as file:
        updates = [line.rstrip() for line in file]
    
    with open('testinput5a.txt', 'r') as file:
        rules = [line.rstrip() for line in file]
    with open('testinput5b.txt', 'r') as file:
        updates = [line.rstrip() for line in file]

    return rules, updates
    
