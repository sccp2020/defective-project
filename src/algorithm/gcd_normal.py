# gcd:
# Given 2 integers (as A, B), return GCD(A, B)
#   ref. https://ja.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E5%85%AC%E7%B4%84%E6%95%B0
# NOTE: SHOULD use Euclidean Algorithm
#       CANNOT use library

def gcd(a, b):
    
    if a < b:
        tmp = b
        b = a
        a = tmp

    r = a % b
    while(r != 0):
        a = b
        b = r
        r = a % b

    return b
