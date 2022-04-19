from sys import stdin, stdout 
# Code by Pablo Maya Villegas & Andres Echeverri Jaramillo
# Created 4 April 2022 
# Modified 18 April 2022

# Reads the first line and starts a cicle for the number of sets
def Start():
    n = int(stdin.readline().strip())
    on = n + 1
    string = ''

    # Loops every case
    while n > 0:
        string += 'Case #' + str(on - n) + ': '
        string += Case() + '\n'
        n -= 1
    stdout.write(string)

    # Code to print to a txt file the output for easy uDebug testing
    #f = open("output.txt", "w")
    #f.write(string)
    #f.close()

# The code to read a single case, it gets the n and m 
# it reads the prohibited pair in an array, they are stored in a matrix
def Case():
    ins = stdin.readline().strip().split()
    n = int(ins[0])
    m = int(ins[1])

    # List of strings where at location n are stored the prohibited pairs of that student
    # Example, at if at trouble[8] is stored '3 5' then 8 3 and 8 5 are prohibited
    trouble = [''] * (n+1)
    loop = 0
    while loop < m:
        x = stdin.readline().strip().split()
        y = sorted([int(x[0]), int(x[1])])
        
        trouble[y[1]] += str(y[0]) + ' '
        loop += 1
    
    return Recursion(['1'], [], n, 1, 0, 1, trouble)
    
# Recursive method
# A & B = the two classrooms were students are stored
# n = the number of students, it's used as a limit
# ma & mb = the limit of weight currently of that classroom
# la & lb = the size of the classrooms
# start = the current student to be classified, starts at 1 and gets to n
# trouble = the matrix of problematic pairs
def Recursion(A, B, n, la, lb, start, trouble):
    # If the classrooms are full or if all the students are assigned ends recursion
    if la + lb == n:
        string = str(la) + '\n'
        for a in A:
            string += a + ' '
        return string.strip()

    # Gets the weight (number of prohibited pairs) of the current number (start) in both classrooms
    start += 1
    weightA = 0
    for a in A:
        if a in trouble[start]:
            weightA += 1
    weightB = 0
    for b in B:
        if b in trouble[start]:
            weightB += 1

    # If the weight is the same in both classrooms, the student is moved to the A class
    if weightA == weightB:
        A.append(str(start))
        la += 1
        return Recursion(A, B, n, la, lb, start, trouble)
            
    # Moves the student to the classroom that has the least trouble pairs (lowest weight)
    if weightA > weightB:
        B.append(str(start))
        lb += 1
        return Recursion(A, B, n, la, lb, start, trouble)
    else:
        A.append(str(start))
        la += 1
        return Recursion(A, B, n, la, lb, start, trouble)
        
Start()
