def add_second_digit_number(num1, num2):
    num1=str(num1)
    num2=str(num2)
    list_num1=list(num1)
    list_num2=list(num2)

    return (int)(list_num1[-2])+(int)(list_num2[-2])
