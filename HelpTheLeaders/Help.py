from sys import stdin, stdout
# Code by Pablo Maya Villegas
# 14 February 2022

# Reads the first line and starts a cicle for the number of sets
def Start():
    n = int(stdin.readline().strip())
    on = n + 1
    string = ''

    # Loop that works for every set
    while n > 0:
        string += 'Set ' + str(on - n) + ':\n'
        string += Set()
        string += '\n'
        n -= 1
    stdout.write(string)

    # Code to print to a txt file the output for easy uDebug testing
    f = open("output.txt", "w")
    f.write(string)
    f.close()
    
# The code to read a single set, it gets the 3 inicial values and
# two lists of the starter topics and the prohibited combinations
def Set():
    ins = stdin.readline().strip().split(" ")
    t = int(ins[0])
    p = int(ins[1])
    s = int(ins[2])

    start = []
    prohibited = []

    # Reads the starter topics and stores them in an array
    while t > 0:
        start.append(stdin.readline().strip().upper())# Removes the \n character and upper cases it
        t -= 1
    start.sort()                     # Sorts the list alphabetically
    start.sort(key=len, reverse=True)# Sorts the list by size, longest is first
    
    # Reads the prohibited combinations and stores them in an array
    while p > 0:
        temp = stdin.readline().strip().upper().split()
        temp.sort()
        temp.sort(key=len, reverse=True)
        prohibited.append(' '.join(temp))
        p -= 1

    t = len(start)
    x = 0
    A = [-1] * s
    string = ''
    # Starts the tree dividing it by all the possible starting topics
    while x < t:
        string += Recursion(A, x, s, t, 0, start, prohibited)
        x += 1
    return string


# Recursive class
# A = Backtraking array, starting value is [-1] * s (s = 3 then [-1,-1,-1])
# x = Current position of the start array
# s = Number of desired topics in a combination
# t = Number of elements in the start array
# start = The starter topics array
# prohibited = The prohibited combinations
def Recursion(A, x, s, t, i, start, prohibited):
    if A[i] == -1 and x < t:
        A[i] = start[x] # Places the topic in the combination
        x += 1    
        string = ''
        # If the desired s# combination is achived, cheks if its Valid
        # Removes the last topic to backtrack to another branch and keep the same array
        if s == 1:
            string += Valid(' '.join(map(str, A)), len(A), prohibited)
            A[i] = -1
            return string

        # Divides the tree by all the possible combinations of topics on the right
        # This way topics on the left  don't get repeated
        l = x
        while l < t:
            string += Recursion(A, l, s - 1, t, i + 1, start, prohibited)
            l += 1

        A[i] = -1 # Removes the topic to backtrack 
        return string


# Checks if the current combination is valid or prohibited
def Valid(A, s, prohibited):
    for p in prohibited:
        if p == A:
            return ''
        # If s is >= 3 then there could be a prohibited pair with another word in the middle
        elif s >= 3:
            z = p.split()
            # If both elements of the prohibited list are in the combination, it's discarded
            if (z[0] + " ") in (A + " ") and (z[1] + " ") in (A + " "): 
                return ''
    return A + '\n' # It's valid

Start()