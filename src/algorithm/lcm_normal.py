# lcm:
# Given 2 integers (as A, B), return LCM(A, B)
#   ref. https://ja.wikipedia.org/wiki/%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B0
# NOTE: if already solved GCD, you can use.
#       CANNOT use library

def lcm(a, b):
    storea = a
    storeb = b
    if(b > a):
        temp = a
        a = b
        b = temp

    r = a % b
    while(r != 0):
        a = b
        b = r
        r = a % b

    
    return (storea * storeb) / b
