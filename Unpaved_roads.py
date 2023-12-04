def findValues(startPos, grid, gamma, goals, teleporter, livingCost, movement):
    wall = True
    x = startPos[0]
    y = startPos[1]
    vals = [0,0,0]
    maximum = ["dir", -99999.99]

    if [x,y] == goals[1]:
        print("[",x,",",y,"] is a goal")
        return 1
    if [x,y] == goals[0]:
        print("[",x,",",y,"] is a hole")
        return -1
        

    if [x,y] in teleporter:
        if wall == False:
            print("[",x,",",y,"] (teleporter WIP):")
            if [x,y] == teleporter[0]:
                new_x,new_y = teleporter[1]
            else:
                new_x, new_y = teleporter[0]
        else:
            print("[",x,",",y,"] is a wall")
            return 0
    else:
        print("[",x,",",y,"]:")

    for k in movement:
        new_x = x + movement[k][0]
        if new_x < 0 or new_x >= 4:
            new_x = x #bounces back
        new_y = y + movement[k][1]
        if new_y < 0 or new_y >= 5:
            new_y = y #bounces back
        if wall == True and [new_x,new_y] in teleporter:
            new_x = x
            new_y = y
        
        vals[0] = grid[new_x][new_y]
        
        if k == "top" or k == "down":
            new_x = x #reset x movement
            for j in [1,-1]:
                new_y = y + j
                if new_y < 0 or new_y >= 5:
                    new_y = y #bounces back
                if wall == True and [new_x,new_y] in teleporter:
                    new_y = y              
                vals[j] = grid[new_x][new_y]
        else:
            new_y = y #reset y movement
            for j in [1,-1]:
                new_x = x + j
                if new_x < 0 or new_x >= 4:
                    new_x = x #bounces back
                if wall == True and [new_x,new_y] in teleporter:
                    new_x = x
                vals[j] = grid[new_x][new_y]   

        final_val = 0.2*((vals[1]*gamma)-livingCost) + 0.2*((vals[-1]*gamma)-livingCost) + 0.6*((vals[0]*gamma)-livingCost)
        final_val = round(final_val, 2)

        print(f"{k} : {final_val} ", end=" ")
        print("")
        #print(vals)
        
        if final_val >= maximum[1]:
            maximum[0] = k
            maximum[1] = final_val
    print(f"\nBest: {maximum[0]} = {maximum[1]}\n")
    return maximum[1]

def main():
    gamma = 0.9
    livingCost = 0.1
    teleporter = [
            [0,1],
            [2,3]
            ]
    goals = [
        [1,1],
        [1,3]
        ]

    movement = {"top": [-1,0], "down": [1,0], "left": [0,-1], "right": [0,1]}

    grid = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
        ]
        
    new_grid = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
        ]
            
    l = 3

    for r in range(0,l):
        print("======================================================================")
        print("k=",r+1)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                new_grid[x][y] = findValues([x,y], grid, gamma, goals, teleporter, livingCost,movement)

        print("==============final grid==============")
        print("K=",r+1)
        for x in range(len(new_grid)):
            for y in range(len(new_grid[x])):
                print(new_grid[x][y], end="\t\t")
            print("")
            grid[x] = new_grid[x].copy()

if __name__=="__main__":
    main()