tree_grid = []

total_visible = 0
isVisible = True

total_trees_right = 0
total_trees_left = 0
total_trees_up = 0
total_trees_down = 0


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
                tempCol -= 1
                while(tempCol != 0):
                    #print(interior_tree, tree_grid[eachRow][tempCol-1], "INNER A")
                    if(interior_tree <= tree_grid[eachRow][tempCol-1]):
                        isVisible = False
                        break
                    tempCol -= 1
                if(isVisible):
                    #print("PASSED A", interior_tree, eachRow, eachColumn)
                    total_visible += 1
                    continue
                else:
                    isVisible = True
                    tempCol = eachColumn
            
            #RIGHT  
            if(interior_tree > tree_grid[eachRow][eachColumn+1]):
                #print(interior_tree, tree_grid[eachRow][eachColumn+1], "B")
                tempCol += 1
                while(tempCol != len(tree_grid[eachRow]) - 1):
                    #print(interior_tree, tree_grid[eachRow][tempCol+1], "INNER B")
                    if(interior_tree <= tree_grid[eachRow][tempCol+1]):
                        isVisible = False
                        break
                    tempCol += 1
                if(isVisible):
                    #print("PASSED B", interior_tree, eachRow, eachColumn)
                    total_visible += 1
                    continue
                else:
                    isVisible = True
            
            #UP     
            if(interior_tree > tree_grid[eachRow-1][eachColumn]):
                #print(interior_tree, tree_grid[eachRow-1][eachColumn], "C")
                tempRow -= 1
                while(tempRow != 0):
                    #print(interior_tree, tree_grid[tempRow-1][eachColumn], "INNER C")
                    if(interior_tree <= tree_grid[tempRow-1][eachColumn]):
                        isVisible = False
                        break
                    tempRow -= 1
                if(isVisible):
                    #print("PASSED C", interior_tree, eachRow, eachColumn)
                    total_visible += 1
                    continue
                else:
                    isVisible = True
                    tempRow = eachRow
            
            #DOWN    
            if(interior_tree > tree_grid[eachRow+1][eachColumn]):
                #print(interior_tree, tree_grid[eachRow+1][eachColumn], "D")
                tempRow += 1
                while(tempRow != len(tree_grid) - 1):
                    #print(interior_tree, tree_grid[tempRow+1][eachColumn], "INNER D")
                    if(interior_tree <= tree_grid[tempRow+1][eachColumn]):
                        isVisible = False
                        break
                    tempRow += 1
                if(isVisible):
                    #print("PASSED D", interior_tree, eachRow, eachColumn)
                    total_visible += 1
                    continue
                else:
                    isVisible = True
print(total_visible)
#print(tree_grid)