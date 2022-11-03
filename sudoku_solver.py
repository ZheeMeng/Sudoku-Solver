import sys

#pre-process function
#takes in user file and check if it is a valid sudoku grid
def pre_process(sudoku_input):
    sudoku=open(sudoku_input,'r')
    lines=sudoku.readlines()
    grid=[]

    for line in lines:
        grid.append(line.split())

    for i in range(9):
        for j in range(9):
            grid[i][j]=int(grid[i][j])

    if len(grid[:])!=9 or len(grid)!=9:
        raise Exception("Invalid grid format")

    return grid

#check function
#to check if n is repeated in the respective row, column and subgrid
def check(row,col,n):
    global grid
    no_repeats=True

    #row check
    for i in range(9):
        if grid[row][i]==n:
            no_repeats=False
    
    #col check
    for i in range(9):
        if grid[i][col]==n:
            no_repeats=False

    #subgrid check
    sg_x=(col//3)*3
    sg_y=(row//3)*3

    for i in range(3):
        for j in range(3):
            if grid[sg_y+i][sg_x+j]==n:
                no_repeats=False

    return no_repeats

#main function
#responsible for backtracking and the solution of the grid, shows possible solution and where the programme exits
def solve():
    global grid
    global solution_count

    for row in range(9):
        for col in range(9):
            if grid[row][col]==0:
                for n in range(1,10):
                    if check(row,col,n):
                        grid[row][col]=n
                        solve()
                        grid[row][col]=0
                        
                return 

    output()
    solution_count+=1
    input("Total solutions: %d"%solution_count)

#output function
#print out the sudoku solution in a clearer format
def output():
    global grid

    for row in grid:
        print(row)

#driver function
def driver():
    global grid 
    global solution_count

    #check the number of arguments
    if len(sys.argv)==2:
        grid=pre_process(sys.argv[1]) 
        solution_count=0
        solve()

    else:
        raise Exception("Please input in the following format: 'python sudoku_solver.py user_file'")

driver()