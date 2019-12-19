# Given an Integer as N, Return N'th Fibonacci number
#
# Definition:
#   F is Fibonacci number,
#     F[0] == 0
#     F[1] == 1

def fib(N):
    F = [0] * 100
    F[0] = 0;
    F[1] = 1;
    count = 2;
    
    while(count <= N):
        F[count] = F[count-2] + F[count-1]
        count = count + 1
        
    return F[N]
