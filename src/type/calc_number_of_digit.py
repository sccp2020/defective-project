def calc_number_of_digit(num):
    cnt = 0
    while num > 0:
        t = num%10
        for j in range(10):
            if t == j : cnt += 1
        num = num//10
    return cnt
