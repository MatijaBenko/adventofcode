all_dir = {'/': []}
dir_tree = {'/': []}
curr_dir = '/'
stack = []
head_dir = ''
with open("input.txt", "r") as f:
    commands = [line.strip().split(" ") for line in f]
    for eachCommand in commands:
        print(eachCommand, "EACH COMMAND")
        if (eachCommand[0] == "dir"):
            if (eachCommand[1] not in dir_tree):
                dir_tree[head_dir].append(eachCommand[1])
                dir_tree[eachCommand[1]] = []
                if(eachCommand[1] not in all_dir):
                    all_dir[eachCommand[1]] = []
                
        elif (eachCommand[0] == "$"):
            if (eachCommand[1] == "ls"):
                continue
            elif (eachCommand[1] == "cd"):
                curr_dir = eachCommand[2]
                if (curr_dir != ".."):
                    stack.append(curr_dir)
                    head_dir = curr_dir
                elif (curr_dir == ".."):
                    if (len(stack) == 1):
                        continue
                    else:
                        stack.pop()
                        head_dir = stack[-1]
                        print(all_dir, "ALl Directories")
                        print(dir_tree, "TREE")
                        print(head_dir, "HEAD")
                        print(stack, "STACK")
                        continue

        else:
            if (eachCommand[0].isnumeric()):
                all_dir[curr_dir].append(int(eachCommand[0]))
        print(all_dir, "ALl Directories")
        print(dir_tree, "TREE")
        print(head_dir, "HEAD")
        print(stack, "STACK")



# total = 0
# min_value = 0
# print(all_dir, "ALl Directories")
# print(dir_tree, "TREE")

# for eachKey in dir_tree.items():
#     total += sum(all_dir[eachKey[0]])
#     for eachValue in eachKey[1]:
#         total += sum(all_dir[eachValue])
#     all_dir[eachKey[0]] = total
#     total = 0
    
# #print(all_dir, "ALl Directories")
# del all_dir['/']
# del dir_tree['/']

# print(all_dir, "ALl Directories")
# print(dir_tree, "TREE")

# for eachKey in all_dir:
#     if min_value == 0:
#         min_value = all_dir[eachKey]
#     else:
#         if (min_value + all_dir[eachKey] < 100000):
#             min_value += all_dir[eachKey]
#             break
            
# print(min_value)
        