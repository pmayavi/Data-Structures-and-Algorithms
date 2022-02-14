#Code by Pablo Maya Villegas
import sys

def main(x, poly):
    len = poly.pop(0)
    sum = poly.pop(0)
    return polynomium(x, 1, len, sum, poly)


def polynomium(x, xpot, len, sum, poly):
    len -= 1
    if len == 0:
        print(sum)
        return sum

    xpot *= x
    sum += xpot * poly.pop(0)
    return polynomium(x, xpot, len, sum, poly)

if __name__ == "__main__":
    main(int(sys.argv[1]),list(map(int, sys.argv[2].split(","))))

'''
To run from the command line use an argument as follows:
python Polynomial.py 2 "4,6,0,2,4"
python Polynomial.py 1 "3,1,2,3"
python Polynomial.py 5 "5,5,5,5,5,5"

The first argument, the 2, is the value of x 
The string is the list of the coefficients as such: "Length,X,X^2,X^3"
The length of the list can be as long as desiered

 X = 2 
 4X^3 + 2x^2 + 6 
 = 4*8 + 2*4 + 0*2 + 6  =  46
'''