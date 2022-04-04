from sys import stdin, stdout 
# Code by Pablo Maya Villegas
# 4 April 2022

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
    ma = m/2

    trouble = []
    while m > 0:
        x = stdin.readline().strip().split()
        y = [int(x[0]), int(x[1])]
        if y[0] > y[1]:
            temp = y[0]
            y[0] = y[1]
            y[1] = temp
        trouble.append(y)
        m -= 1

    return Recursion([1], [], n, ma, ma, 1, 0, 1, trouble)
    
# Recursive method
# A & B = the two classrooms were students are stored
# n = the number of students, it's used as a limit
# ma & mb = the limit of weight currently of that classroom
# la & lb = the size of the classrooms
# start = the current student to be classified, starts at 1 and gets to n
# trouble = the matrix of problematic pairs
def Recursion(A, B, n, ma, mb, la, lb, start, trouble):
    # If the classrooms are full or if all the students are assigned ends recursion
    if la + lb == n or start > n:
        string = str(la) + '\n'
        for a in A:
            string += str(a) + ' '
        return string.strip()

    # Gets the weight (number of prohibited pairs) of the current number (start) in both classrooms
    start += 1
    weightA = 0
    for a in A:
        for t in trouble:
            if a == t[0] and start == t[1]:
                weightA += 1
    weightB = 0
    for a in B:
        for t in trouble:
            if a == t[0] and start == t[1]:
                weightB += 1

    # If the weight is the same in both classrooms, the student is moved to the A class
    if weightA == weightB:
        ma -= weightA
        A.append(start)
        la += 1
        return Recursion(A, B, n, ma, mb, la, lb, start, trouble)
            
    # Moves the student to the classroom that has the least trouble pairs (lowest weight)
    if weightA > weightB:
        mb -= weightB
        B.append(start)
        lb += 1
        return Recursion(A, B, n, ma, mb, la, lb, start, trouble)
    else:
        ma -= weightA
        A.append(start)
        la += 1
        return Recursion(A, B, n, ma, mb, la, lb, start, trouble)
        
Start()
