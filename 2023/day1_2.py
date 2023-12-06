with open('2023/test_input1_1.txt', 'r') as file:
    lines = [line.rstrip() for line in file]

val_sum = 0
num_words = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

for line in lines:
    nums = [[0,0],[0,0]]
    
    for index, char in enumerate(line):
        if char.isdigit():
            nums[1] = [index,int(char)]
            if nums[0][1] == 0:
                nums[0] = [index,int(char)]

    for word in num_words:
        if 0 <= line.find(word) < nums[0][0]:
            nums[0] = [line.find(word), num_words[word]]
        
        rev_num_check = line[::-1].find(word[::-1])
        if rev_num_check > -1:
            last_word_index = len(line) - rev_num_check - len(word)
            if last_word_index > nums[1][0]:
                nums[1] = [last_word_index, num_words[word]]
        
    val_sum += 10*nums[0][1] + nums[1][1]

    print(val_sum)