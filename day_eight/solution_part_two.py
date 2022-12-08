tree_grid = []

total = 0
total_visible = 0
isVisible = True

total_trees_right = 0
total_trees_left = 0
total_trees_up = 0
total_trees_down = 0

scenic_trees_score = []


with open("input.txt", "r") as f:
    eachLine = [line.strip() for line in f]
    for eachList in eachLine:
        temp = [int(d) for d in str(eachList)]
        tree_grid.append(temp)
    
    total_visible += (len(tree_grid[0]) + len(tree_grid[-1]))
    for eachRow in range(0,len(tree_grid)-2):
        total_visible += 2
    
        
    for eachRow in range(1,len(tree_grid)-1):
        for eachColumn in range(1,len(tree_grid[eachRow])-1):
            interior_tree = tree_grid[eachRow][eachColumn]
            tempRow = eachRow
            tempCol = eachColumn
            
            #print(interior_tree, "CURR")
            # LEFT
            if(interior_tree > tree_grid[eachRow][eachColumn-1]):
                #print(interior_tree, tree_grid[eachRow][eachColumn-1], "A")
                total_trees_left += 1
                tempCol -= 1
                while(tempCol != 0):
                    #print(interior_tree, tree_grid[eachRow][tempCol-1], "INNER A")
                    if(interior_tree > tree_grid[eachRow][tempCol-1]):
                        total_trees_left += 1
                    elif(interior_tree <= tree_grid[eachRow][tempCol-1]):
                        total_trees_left += 1
                        break
                    tempCol -= 1 
            else:
                total_trees_left += 1
            tempCol = eachColumn
            
            
            #RIGHT  
            if(interior_tree > tree_grid[eachRow][eachColumn+1]):
                #print(interior_tree, tree_grid[eachRow][eachColumn+1], "B")
                total_trees_right += 1
                tempCol += 1
                #print(total_trees_right, "BEFORE")
                while(tempCol != len(tree_grid[eachRow]) - 1):
                    #print(interior_tree, tree_grid[eachRow][tempCol+1], "INNER B")
                    if(interior_tree > tree_grid[eachRow][tempCol+1]):
                        total_trees_right += 1
                        #print(total_trees_right, "RIGHT")
                    elif(interior_tree <= tree_grid[eachRow][tempCol+1]):
                        total_trees_right += 1
                        break
                    tempCol += 1
            else:
                total_trees_right += 1
                
            
            #UP     
            if(interior_tree > tree_grid[eachRow-1][eachColumn]):
                #print(interior_tree, tree_grid[eachRow-1][eachColumn], "C")
                total_trees_up += 1
                tempRow -= 1
                while(tempRow != 0):
                    #print(interior_tree, tree_grid[tempRow-1][eachColumn], "INNER C")
                    if(interior_tree > tree_grid[tempRow-1][eachColumn]):
                        total_trees_up += 1
                    elif(interior_tree <= tree_grid[tempRow-1][eachColumn]):
                        total_trees_up +=1
                        break
                    tempRow -= 1
            else:
                total_trees_up += 1
            tempRow = eachRow
                
            
            #DOWN    
            if(interior_tree > tree_grid[eachRow+1][eachColumn]):
                #print(interior_tree, tree_grid[eachRow+1][eachColumn], "D")
                total_trees_down += 1
                tempRow += 1
                #print(len(tree_grid), "LEN" , tempRow)
                while(tempRow != len(tree_grid) - 1):
                    #print(interior_tree, tree_grid[tempRow+1][eachColumn], "INNER D")
                    if(interior_tree > tree_grid[tempRow+1][eachColumn]):
                        total_trees_down += 1
                    elif(interior_tree <= tree_grid[tempRow+1][eachColumn]):
                        total_trees_down += 1
                        break
                    tempRow += 1
            else:
                total_trees_down += 1
                
            #print("DOWN",total_trees_down, "UP",total_trees_up,"LEFT", total_trees_left, "RIGHT",total_trees_right)
            total += (total_trees_down * total_trees_left * total_trees_right * total_trees_up)
            scenic_trees_score.append(total)
            total_trees_up = 0
            total_trees_down = 0
            total_trees_left = 0
            total_trees_right = 0
            total = 0
#print(total_visible)
#print(scenic_trees_score)
print(max(scenic_trees_score))
