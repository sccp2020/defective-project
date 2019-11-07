def add_second_digit_number(num1, num2):
    # return num1 + num2
    num1 = (num1%100 - num1%10) // 10
    num2 = (num2%100 - num2%10) // 10
    return num1 + num2
