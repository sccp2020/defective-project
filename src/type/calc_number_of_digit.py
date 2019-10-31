def calc_number_of_digit(num):
    cnt=len(str(num))
    for i in range(len(str(num))):
        if ord(str(num)[i])<48 or ord(str(num)[i])>57:
            cnt-=1
    return cnt
