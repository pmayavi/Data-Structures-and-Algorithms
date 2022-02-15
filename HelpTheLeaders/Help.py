from sys import stdin, stdout
from itertools import combinations
# Code by Pablo Maya Villegas
# 14 February 2022

# Reads the first line and starts a cicle for the number of sets
def Start():
    n = int(stdin.readline().strip())
    on = n + 1
    string = ""

    while n > 0:
        combs = Set()
        string = Save(string, on - n, combs)
        n -= 1

    # Writes a txt file with the correct combinations
    stdout.write(string)

# The code for a single set, it gets the 3 inicial values and
# two lists of the possible combinations and the prohibited combinations
def Set():
    ins = stdin.readline().strip().split(" ")
    t = int(ins[0])
    p = int(ins[1])
    s = int(ins[2])

    start = []
    prohibited = []
    while t > 0:
        start.append(stdin.readline()[:-1].upper())
        t -= 1
    start.sort()                     # Sorts the list alphabetically
    start.sort(key=len, reverse=True)# Sorts the list by size, longest is first
    while p > 0:
        p1 = stdin.readline().strip().upper()
        p2 = p1.split(" ")
        p2.sort()
        p2.sort(key=len, reverse=True)
        prohibited.append(' '.join(p2))
        p -= 1
    prohibited.sort()
    prohibited.sort(key=len, reverse=True)


    return Combinations(start, prohibited, s)

# Creates the possible combinations with the help of the itertool combinations
# Removes the combinations that are prohibited
def Combinations(start, prohibited, s):
    c = combinations(start, s)
    combs = [' '.join(i) for i in c]
    remove = []
    for c in combs:
        for p in prohibited:
            if p == c:
                remove.append(c)
            elif s >= 3:
                t = True
                z = p.split(" ")
                for x in z:
                    if (x + " ") not in (c + " "):
                        t = False
                if t:
                    remove.append(c)

    for r in remove:
        if r in combs:
            combs.remove(r)

    return combs

# Saves the Set to a string to be printed or written later
def Save(string, n, combs):
    string += "Set " + str(n) + ":\n"
    for x in combs:
        string += "".join(x) + "\n"
    string += "\n"
    return string


Start()
