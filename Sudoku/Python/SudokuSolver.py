# Method to read a Sudoku.txt file, the first line is the size of the sudoku
# for example 3x4 where 4 is length of x (sx) and 3 is length of y (sy) of a square
def read():
    f = open("3x3.txt", "r")
    s = f.readline().strip().split('x')
    sx = int(s[0])
    sy = int(s[1])

    # Creates a matrix filled with 0s of size sx * sy
    lis = [0] * (sx*sy)
    sudoku = []
    for x in range(sx*sy):
        sudoku.append(lis.copy())

    # Stores the values read in the file, every number is stored at their location
    s = f.readline().strip().split()
    cy = 0
    while len(s) > 1:
        cx = 0
        for x in s:
            sudoku[cy][cx] = int(x)
            cx += 1
        s = f.readline().strip().split()
        cy += 1

    solve(sudoku, sy, sx, 0)
    f.close()

# Method that validates if a single number n can be stored at location [y][x]    
def validate(sudoku, sy, sx, y, x, n):
    for num in range(sx*sy):
        # Checks the horizontal line
        if n == sudoku[y][num]:
            return False
        # Checks the vertical line
        if n == sudoku[num][x]:
            return False
    
    # Finds the first location in a square
    y0 = (y//sy)*sy
    x0 = (x//sx)*sx
    # Checks the square by starting at the first location and traveling for sy * sx times
    for i in range(sy):
        for j in range(sx):
            if n == sudoku[y0 + i][x0 + j]:
                return False

    return True

# Recursive method that finds solutions of a Sudoku
# Using backtracking it tries multiple solutions and backtracks when necesary
def solve(sudoku, sy, sx, y0):
    for y in range(y0,sx*sy):
        for x in range(sx*sy):
            # If the location is empty
            if sudoku[y][x] == 0:
                # Creates sx*sy branches, so in a 3x3 Sudoku it creates 9 branches where 
                # numbers 1-9 are validated and tested
                for n in range(1,(sx*sy) + 1):
                    if validate(sudoku, sy, sx, y, x, n):
                        sudoku[y][x] = n
                        solve(sudoku, sy, sx, y)
                        sudoku[y][x] = 0
                return
    # If the Sudoku arrives here then all values have benn placed and verified, so it's a valid solution
    printSudoku(sudoku)
    input('See more solutions?')

# Method to print a matrix in an orderly fashion
def printSudoku(sudoku):
    for y in sudoku:
        string = ''
        for x in y:
            string += str(x) + ' '
        print(string)

read()