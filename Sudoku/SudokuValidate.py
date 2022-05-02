# Method to read a Sudoku.txt file, the first line is the size of the sudoku
# for example 3x4 where 4 is length of x (sx) and 3 is length of y (sy) of a square
def read():
    f = open("Solved3x3.txt", "r")
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

    validateSudoku(sudoku, sy, sx)
    printSudoku(sudoku)
    f.close()

# Method that validates if a Sudoku is correct, wrong or has empty spaces
def validateSudoku(sudoku, sy, sx):
    cy = 0
    for y in sudoku:   
        cx = 0
        for x in y:
            # Checks every value if one is 0 then its incomplete
            if x == 0:
                print('Incomplete Sudoku with empty spaces detected\n')
                return False
            # Checks every value if one is invalid then is wrong
            # Uses the method validate that prints where the conflict was found
            if not validate(sudoku, sy, sx, cy, cx, x):
                print('Wrong answer')
                return False
            cx += 1
        cy += 1
    # Every number passes the test so the Sudoku is correct
    print('Correct!')
    return True

# Method that validates if a single number n can be stored at location [y][x]       
def validate(sudoku, sy, sx, y, x, n):
    for num in range(sx*sy):
        # Checks the horizontal line
        if n == sudoku[y][num] and num != x:
            error(y, x, y, num)
            return False
        # Checks the vertical line
        if n == sudoku[num][x] and num != y:
            error(y, x, num, x)
            return False
    
    # Finds the first location in a square
    y0 = (y//sy)*sy
    x0 = (x//sx)*sx
    # Checks the square by starting at the first location and traveling for sy * sx times
    for i in range(sy):
        for j in range(sx):
            if n == sudoku[y0 + i][x0 + j] and (y0 + i != y or x0 + j != x):
                error(y, x, x0 + i, y0 + j)
                return False

    return True

# Method that prints where an error was located
def error(y, x, yj, xi):
    string = 'Conflict encountered at '
    string += str(y+1) + ' ' + str(x+1) 
    string += ' with '
    string += str(yj+1) + ' ' + str(xi+1)  
    print(string)

# Method to print a matrix in an orderly fashion
def printSudoku(sudoku):
    for y in sudoku:
        string = ''
        for x in y:
            string += str(x) + ' '
        print(string)

read()