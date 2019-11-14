def round_off_nth_digit(num, digit):
    count = digit
    x = num + 0.0
    while(count == 0):
        x = x * 10
        count -= 1
    ans = int(x + 0.5)
    count = digit
    x = ans + 0.0
    while(count == 0):
        x = x / 10
        count -= 1
    return x

# hint : 小数点n桁目を四捨五入する関数
# e.g. : (123.456, 2) -> 123.46
