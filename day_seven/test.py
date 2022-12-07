all_dir = {}
dir_tree = {}
order_dir = []
path = ''

with open("input.txt", "r") as f:
    commands = [line.strip().split(" ") for line in f]
    for eachCommand in commands:
        #print(eachCommand)
        if (eachCommand[0] == "$"):
            if (eachCommand[1] == "ls"):
                continue
            elif (eachCommand[1] == "cd"):
                path = ''
                
                if(eachCommand[2] != ".."):
                    order_dir.append(eachCommand[2])
                    
                if eachCommand[2] == "..":
                    order_dir.pop()
                    for eachItem in order_dir:
                        path += eachItem
                else:
                    for eachItem in order_dir:
                        path += eachItem
                    if(path not in all_dir):
                        all_dir[path] = 0
                    if (path not in dir_tree):
                        dir_tree[path] = []
        elif (eachCommand[0] == "dir"):
            temp_list = dir_tree[path]
            temp_list.append(eachCommand[1])
            dir_tree[path] = temp_list
        else:
            if (eachCommand[0].isnumeric()):
                all_dir[path]+=int(eachCommand[0])
                temp_path = path
                if(len(temp_path) > 1):
                    while len(temp_path) > 1:
                        if(temp_path[:-1] in all_dir):
                            all_dir[temp_path[:-1]] += int(eachCommand[0])
                        temp_path = temp_path[:-1]

min_value = 0
total = 0

limit = 70000000
memory_available = limit - all_dir['/']
goal = 30000000 - memory_available

print(goal, "GOAL")

for eachPair in all_dir.items():
    size = eachPair[1]
    if(min_value == 0 and size >= goal):
        min_value = size
    elif(size >= goal and size < min_value):
        min_value = size
        
        


print(min_value)
#print(all_dir)
#print(dir_tree)
