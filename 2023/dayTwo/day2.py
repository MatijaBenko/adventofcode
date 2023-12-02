# totalReds = 0
# totalBlues = 0
# totalGreens = 0
# gamePass = True
# gameID = []

# allGamesPassed = []


# with open("adventofcode/2023/dayTwo/test.txt") as topo_file:
#     for eachLine in topo_file:
#         test = eachLine.strip().split(":")
#         gameID = test[0].split(" ")
#         eachGameSet = test[1].split(";")
#         for eachRound in eachGameSet:
#             colors = eachRound.split(",")
#             for eachColor in colors:
#                 draw = eachColor.split(" ")
#                 if(draw[2] == "red"):
#                     totalReds += int(draw[1])
#                 if(draw[2] == "blue"):
#                     totalBlues += int(draw[1])
#                 if(draw[2] == "green"):
#                     totalGreens += int(draw[1])
#             if(totalReds > 12 or totalGreens > 13 or totalBlues > 14):
#                 gamePass = False
#                 totalBlues = 0
#                 totalGreens = 0
#                 totalReds = 0
#                 break
#             totalBlues = 0
#             totalGreens = 0
#             totalReds = 0
#         if(gamePass):
#             allGamesPassed.append(int(gameID[1]))
#         gamePass = True
            
#     print(sum(allGamesPassed))

totalReds = 1
totalBlues = 1
totalGreens = 1
gamePass = True
gameID = []

powerList = []


with open("adventofcode/2023/dayTwo/test.txt") as topo_file:
    for eachLine in topo_file:
        test = eachLine.strip().split(":")
        gameID = test[0].split(" ")
        eachGameSet = test[1].split(";")
        for eachRound in eachGameSet:
            colors = eachRound.split(",")
            for eachColor in colors:
                print("EACH", eachColor)
                draw = eachColor.split(" ")
                if(draw[2] == "red"):
                    if(totalReds == 1):  
                        totalReds = int(draw[1])
                    elif(totalReds < int(draw[1])):
                        totalReds = int(draw[1])
                if(draw[2] == "blue"):
                    if(totalBlues == 1):
                        totalBlues = int(draw[1])
                    elif(totalBlues < int(draw[1])):
                        totalBlues = int(draw[1])
                if(draw[2] == "green"):
                    if(totalGreens == 1):
                        totalGreens = int(draw[1])
                    elif(totalGreens < int(draw[1])):
                        totalGreens = int(draw[1])
        totalPower = totalReds * totalBlues * totalGreens
        powerList.append(totalPower)
        totalBlues=1
        totalReds=1
        totalGreens=1