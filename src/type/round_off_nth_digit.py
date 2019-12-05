def round_off_nth_digit(num, digit):
    count = digit
    val = 1
    while(count > 0):
        val = val * 10
        count -= 1
    x = (num * val) + 0.5
    y = int(x)
    ans = float(y) / val
    return ans

# hint : 小数点n桁目を四捨五入する関数
# e.g. : (123.456, 2) -> 123.46
