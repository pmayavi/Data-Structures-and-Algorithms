from random import randint, random, shuffle
from tkinter import N 
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

    randomize(sudoku, sy, sx)
    f.close()

# https://stackoverflow.com/questions/6924216/how-to-generate-sudoku-boards-with-unique-solutions
def randomize(sudoku, sy, sx):
    numbers(sudoku, sy, sx)
    rows(sudoku, sy, sx)
    cols(sudoku, sy, sx)
    rows2(sudoku, sy, sx)
    cols2(sudoku, sy, sx)
    removeNumbers(sudoku, sy, sx)
    printSudoku(sudoku)

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
    solvable = 0
    for y in range(y0,sx*sy):
        for x in range(sx*sy):
            # If the location is empty
            if sudoku[y][x] == 0:
                # Creates sx*sy branches, so in a 3x3 Sudoku it creates 9 branches where 
                # numbers 1-9 are validated and tested
                for n in range(1,(sx*sy) + 1):
                    if validate(sudoku, sy, sx, y, x, n):
                        sudoku[y][x] = n
                        solvable += solve(sudoku, sy, sx, y)
                        sudoku[y][x] = 0
                return solvable
    # If the Sudoku arrives here then all values have benn placed and verified, so it's a valid solution
    #printSudoku(sudoku)
    return solvable + 1

def numbers(sudoku, sy, sx):
    for n in range(1, sx*sy):
        rn = randint(1, sx*sy)
        for y in range(sx*sy):
            for x in range(sx*sy):
                if sudoku[x][y] == n:
                    sudoku[x][y] = rn
                elif sudoku[x][y] == rn:
                    sudoku[x][y] = n

def swapRows(sudoku, n1, n2):
    row = sudoku[n1]
    sudoku[n1] = sudoku[n2]
    sudoku[n2] = row

def swapCols(sudoku, r, n1, n2):
    for i in range(r):
        row = sudoku[i][n1]
        sudoku[i][n1] = sudoku[i][n2]
        sudoku[i][n2] = row

def rows(sudoku, sy, sx):
    for n in range(sx*sy):
        rn = randint(0, sy - 1)
        y0 = (n//sy)*sy
        swapRows(sudoku, n, rn + y0)
        
def cols(sudoku, sy, sx):
    for n in range(sx*sy):
        rn = randint(0, sx - 1)
        x0 = (n//sx)*sx
        swapCols(sudoku, sx*sy, n, rn + x0)
        
def rows2(sudoku, sy, sx):
    for n in range(sy):
        rn = randint(0, sy - 1)
        for i in range(sy):
            swapRows(sudoku, n * sy + i, rn * sy + i)

def cols2(sudoku, sy, sx):
    for n in range(sx):
        rn = randint(0, sx - 1)
        for i in range(sx):
            if n * sx + i < sx*sy and rn * sx + i < sx*sy:
                swapCols(sudoku, sx*sy, n * sx + i, rn * sx + i)

def removeNumbers(sudoku, sy, sx):
    sxy = sy*sx
    listMatrix = []
    listMatrix.extend(range(sxy*sxy))
    shuffle(listMatrix)
    for m in listMatrix:
        n = sudoku[m//sxy][m%sxy]
        sudoku[m//sxy][m%sxy] = 0
        if solve(sudoku, sy, sx, 0) != 1:
            sudoku[m//sxy][m%sxy] = n 
        

# Method to print a matrix in an orderly fashion
def printSudoku(sudoku):
    print()
    for y in sudoku:
        string = ''
        for x in y:
            string += str(x) + ' '
        print(string)

read()