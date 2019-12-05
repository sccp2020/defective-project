# lcm:
# Given 2 integers (as A, B), return LCM(A, B)
#   ref. https://ja.wikipedia.org/wiki/%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B0
# NOTE: if already solved GCD, you can use.
#       CANNOT use library
def lcm(a, b):
    ab=a*b
    while(b != 0):
        t = a % b
        a = b
        b = t

    return ab//a
