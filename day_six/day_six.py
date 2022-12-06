with open("input.txt", "r") as f:
    sack = [line.strip() for line in f]
    pos = 13
    currPos = 0
    char = set()
    stack_temp = []

    word = sack[0]

    def helperFun(word):
        for eachCharacter in range(0, len(word)):
            if (len(stack_temp) < 14 and word[eachCharacter] not in char):
                stack_temp.append(word[eachCharacter])
                char.add(word[eachCharacter])
            else:
                char.clear()
                stack_temp.clear()
                print(stack_temp, "HRER")
                return
            
            if len(stack_temp) == 14:
                break
            print(stack_temp)
            
    
    while(len(char) != 14):
        helperFun(word)
        pos +=1
        currPos += 1
        word = word[currPos:]
        currPos = 0
        
        
    print(pos)

    
