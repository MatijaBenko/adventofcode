# with open('input.txt') as topo_file:
#     stringRep = ""
#     for line in topo_file:
#         for eachChar in line:
#             if eachChar.isdigit():
#                 stringRep+= eachChar
#                 break
#         for eachChar in line[::-1]:
#             if eachChar.isdigit():
#                 stringRep+= eachChar
#                 break
#         listNum.append(int(stringRep))
#         stringRep = ""
# print(sum(listNum))

wordSet = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

wordSet2 = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

def Merge(dict1, dict2):
    return(dict2.update(dict1))

def findnth(string, substring, n):
   parts = string.split(substring, n + 1)
   if len(parts) <= n + 1:
      return -1
   return len(string) - len(parts[-1]) - len(substring)

tempDic = {}
tempList = []

tempDic2 = {}
tempList2 = []

result = []
stringTemp = ""
tempLine = ""
tempListFirst = []
tempListSecond = []

indexofFirstChar = 0
indexofSecondChar = 0
with open("input.txt") as topo_file:
    for eachLine in topo_file:
        print(eachLine)
        tempLine = eachLine
        for eachChar in eachLine:
            if eachChar.isdigit():
                indexofFirstChar = eachLine.index(eachChar)
                tempList.append(indexofFirstChar)
                tempDic[indexofFirstChar] = wordSet2[eachChar]
                break
     
        for eachKey in wordSet:
            if eachKey in eachLine:
                tempListFirst.append(eachLine.index(eachKey))
                tempDic[eachLine.index(eachKey)] = eachKey    
                
        if(len(tempListFirst) == 0):
            print()
        else:
            tempListFirst.sort()
            print("TEST", tempList , tempListFirst)
            if(tempList[0] > tempListFirst[0]):
                tempList.clear()
                tempVal = tempDic[tempListFirst[0]]
                tempDic.clear()
                tempDic[tempListFirst[0]] = tempVal
                tempList.append(tempListFirst[0])
            else:
                tempVal = tempDic[tempList[0]]
                tempDic.clear()
                tempDic[tempList[0]] = tempVal
        
        for eachChar in reversed(eachLine):
            if eachChar.isdigit():
                indexofSecondChar = tempLine.rfind(eachChar)
                tempList2.append(indexofSecondChar)
                tempDic2[indexofSecondChar] = wordSet2[eachChar]
                break
    
        for eachKey in reversed(wordSet):
            if eachKey in eachLine:
                if(eachLine.count(eachKey) > 1):
                    tempListSecond.append(findnth(eachLine, eachKey, eachLine.count(eachKey)-1))
                    tempDic2[findnth(eachLine, eachKey, eachLine.count(eachKey)-1)] = eachKey
                else:
                    tempListSecond.append(eachLine.index(eachKey))
                    tempDic2[eachLine.index(eachKey)] = eachKey
        
        if(len(tempListSecond) == 0):
            print()
        else:
            tempListSecond.sort(reverse=True)
            print("TEST2", tempList2 , tempListSecond)
            if(tempList2[0] < tempListSecond[0]):
                tempList2.clear()
                tempVal = tempDic2[tempListSecond[0]]
                tempDic2.clear()
                tempDic2[tempListSecond[0]] = tempVal
                tempList2.append(tempListSecond[0])
            else:
                tempVal = tempDic2[tempList2[0]]
                tempDic2.clear()
                tempDic2[tempList2[0]] = tempVal
        
        list3 = tempList + tempList2
        list3.sort()
        Merge(tempDic,tempDic2)
        stringTemp += wordSet[tempDic2[list3[0]]]
        stringTemp += wordSet[tempDic2[list3[len(list3) - 1]]]
        result.append(int(stringTemp))
        print("RESULT", result)
        stringTemp = ""
        tempDic = {}
        tempList = []
        tempDic2 = {}
        tempList2 = []
        tempListFirst = []
        tempListSecond = []
print(sum(result))
