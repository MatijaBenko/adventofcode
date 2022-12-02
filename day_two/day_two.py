result = []

pointsWon_temp = 0

def rockFunction(playerPick):
    points_temp = 0
    if (playerPick == "X"):
        points_temp += 3
        points_temp += 0
    elif (playerPick == "Y"):
        points_temp += 1
        points_temp += 3
    else:
        points_temp += 2
        points_temp += 6
    return points_temp
        

def paperFunction(playerPick):
    points_temp = 0
    if (playerPick == "X"):
        points_temp += 1
        points_temp += 0
    elif (playerPick == "Y"):
        points_temp += 2
        points_temp += 3
    else:
        points_temp += 3
        points_temp += 6
    return points_temp

def scissorFunction(playerPick):
    points_temp = 0
    if (playerPick == "X"):
        points_temp += 2
        points_temp += 0
    elif (playerPick == "Y"):
        points_temp += 3
        points_temp += 3
    else:
        points_temp += 1
        points_temp += 6
    return points_temp
    


with open("input.txt", "r") as f:
    listRounds = [line.strip() for line in f]
    for eachGame in listRounds:
        if (eachGame[0] == "A"):
            pointsWon_temp += rockFunction(eachGame[2])
        elif(eachGame[0] == "B"):
            pointsWon_temp += paperFunction(eachGame[2])
        elif(eachGame[0] == "C"):
            pointsWon_temp += scissorFunction(eachGame[2])
        result.append(pointsWon_temp)
        pointsWon_temp = 0

print(sum(result))