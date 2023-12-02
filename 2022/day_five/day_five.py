stacks = []
stacks.append(['M', 'J', 'C', 'B', 'F', 'R', "L", 'H'])
stacks.append(['Z', 'C', 'D'])
stacks.append(['H', 'J', 'F', 'C', 'N', 'G', 'W'])
stacks.append(['P', 'J', 'D', 'M', 'T', 'S', 'B'])
stacks.append(['N', 'C', 'D', 'R', 'J'])
stacks.append(['W', 'L', 'D', 'Q', 'P', 'J', 'G', 'Z'])
stacks.append(['P', 'Z', 'T', 'F', 'R', 'H'])
stacks.append(['L', 'V', 'M', 'G'])
stacks.append(['C', 'B', 'G', 'P', 'F', 'Q', 'R', "J"])

pullStacktemp = []
putStacktemp = []
# #Part 1
# with open("input.txt", "r") as f:
#     sack = [line.strip().split(" ") for line in f]
#     for eachAction in sack:
#         print(eachAction)
#         howMany = int(eachAction[1])
#         pullStack = int(eachAction[3]) - 1
#         putStack = int(eachAction[5]) - 1
#         for eachStackOperation in range(0, howMany):
#             pullStacktemp = stacks[pullStack]
#             putStacktemp = stacks[putStack]
#             tempItem = pullStacktemp.pop()
#             putStacktemp.append(tempItem)
#         stacks[pullStack] = pullStacktemp
#         stacks[putStack] = putStacktemp
#         print(stacks)

# result = ''
# for eachCrate in stacks:
#     if len(eachCrate) > 0:
#         result+= eachCrate[-1]


#Part 2
stack_reverse = []
with open("input.txt", "r") as f:
    sack = [line.strip().split(" ") for line in f]
    for eachAction in sack:
        howMany = int(eachAction[1])
        pullStack = int(eachAction[3]) - 1
        putStack = int(eachAction[5]) - 1
        for eachStackOperation in range(0, howMany):
            pullStacktemp = stacks[pullStack]
            putStacktemp = stacks[putStack]
            tempItem = pullStacktemp.pop()
            stack_reverse.append(tempItem)
        for eachElement in range(0, howMany):
            tempItem = stack_reverse.pop()
            putStacktemp.append(tempItem)
        stacks[pullStack] = pullStacktemp
        stacks[putStack] = putStacktemp

result = ''
for eachCrate in stacks:
    if len(eachCrate) > 0:
        result+= eachCrate[-1]
        
print(result)
