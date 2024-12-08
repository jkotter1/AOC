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
    
def makeRuleDict(rules):
    ruleDict = {}
    
    for rule in rules:
        pageNum1, pageNum2 = [int(x) for x in rule.split("|")]
        if pageNum1 not in ruleDict:
            ruleDict[pageNum1]=[pageNum2]
        else:
            ruleDict[pageNum1].append(pageNum2)
            
    return ruleDict
    
def checkUpdate(update, ruleDict): 
    updateList = [int(x) for x in update.split(",")] #each update as list of ints
    inOrder = True
    
    for ind, page in enumerate(updateList):
        for j in range(ind+1, len(updateList)):
            try:
                if updateList[j] not in ruleDict[page]:
                    inOrder = False
                    break
            except KeyError:
                inOrder = False
                break
        if not inOrder:
            break
    
    return inOrder

def purgeInOrder(ruleDict, updates):
    
    for ind, update in enumerate(updates):
        if checkUpdate(update, ruleDict):
            updates.pop(ind)
    
    return updates

def fixOrder(ruleDict, outOfOrder):
    pass


if __name__ == "__main__":
    rules, updates = getInput()
    ruleDict = makeRuleDict(rules)
    toFix = purgeInOrder(ruleDict, updates)
    
    