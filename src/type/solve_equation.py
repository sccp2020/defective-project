# ax + b = 0
import math
def solve_equation(a, b):
    gcd = math.gcd(a,b)
    if ( b % a ) == 0:
        return -1*a//b
    a = str(int(a / gcd))
    b = str(int(b / gcd))
    return ( "-" + b + "/" + a)
