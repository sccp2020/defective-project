def round_off_nth_digit(num, digit):
    num2 = num * 10**digit
    num2 = int(num2)
    l = list(str(num2))
    if int(l[-1]) >= 5:
         num2 = num2+1
    return num2/10**digit

# hint : 小数点n桁目を四捨五入する関数
# e.g. : (123.456, 2) -> 123.46
