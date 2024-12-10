def getInput():
    with open('input7.txt', 'r') as file:
        calib = [line.rstrip() for line in file]
    with open('testinput7.txt', 'r') as file:
        calib = [line.rstrip() for line in file]
    
    for line in calib:
        pass

    return calib



if __name__ == "__main__":
    calib = getInput()