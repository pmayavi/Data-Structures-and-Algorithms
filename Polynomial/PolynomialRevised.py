#Code by Pablo Maya Villegas
import sys

def main(x, poly):
    sum = 0
    xpot = 1
    for y in poly:
        sum += xpot * y
        xpot *= x
    print(sum)
    return sum

if __name__ == "__main__":
    main(int(sys.argv[1]),list(map(int, sys.argv[2].split(","))))

'''
To run from the command line use an argument as follows:
python PolynomialRevised.py 2 "6,0,2,4"
python PolynomialRevised.py 1 "1,2,3"
python PolynomialRevised.py 5 "5,5,5,5,5"

The first argument is the value of x 
The string is the list of the coefficients as such: "X,X^2,X^3"
The length of the list can be as long as desiered

2 "6,0,2,4":
 X = 2 
 4X^3 + 2x^2 + 0x + 6 
 = 4*8 + 2*4 + 0*2 + 6  =  46
'''