def getInput():
    with open('input5a.txt', 'r') as file:
        rules = [line.rstrip() for line in file]
    with open('input5b.txt', 'r') as file:
        updates = [line.rstrip() for line in file]
    
    '''with open('testinput5a.txt', 'r') as file:
        rules = [line.rstrip() for line in file]
    with open('testinput5b.txt', 'r') as file:
        updates = [line.rstrip() for line in file]'''
        
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
    indicesToPurge = []

    for ind, update in enumerate(updates):
        if checkUpdate(update, ruleDict):
            indicesToPurge.append(ind)
    
    for i in reversed(indicesToPurge):
        updates.pop(i)

    return updates

def fixOrder(ruleDict, outOfOrder):
    
    
    for rowIndex, row in enumerate(outOfOrder):
        nums = [int(x) for x in row.split(",")] #each update as list of ints
        orderedUpdates = [None] * len(nums)
        ListSorted = False

        while ListSorted == False:
            orderedUpdates = []
            ListSorted = True
            for ind, pageNum in enumerate(nums):
                orderedUpdates[ind] = pageNum
                
                try: 
                     for j in range(ind+1, len(nums)):
                        if nums[j] not in ruleDict[pageNum]:
                            ListSorted = False
                            orderedUpdates[ind] = nums[j]
                            orderedUpdates[j] = pageNum
                            break
                except KeyError:
                    orderedUpdates[len(nums)-1] = pageNum #If not listed in the rules, put at the end
                    ListSorted = False
                    for j in range(ind+1, len(nums)):
                        orderedUpdates[j-1] = nums[j]
                    break
                        
        nums = orderedUpdates
                    
        orderedUpdates.append(updateList)
        
    return orderedUpdates
                        

def logMidVals(updates):
    midValSum = 0
    
    for update in updates:
        midValSum += int(update[int(len(update)/2)])
    
    return midValSum

if __name__ == "__main__":
    rules, updates = getInput()
    ruleDict = makeRuleDict(rules)
    toFix = purgeInOrder(ruleDict, updates)
    fixedOrder = fixOrder(ruleDict, toFix)
    print(logMidVals(fixedOrder))
    