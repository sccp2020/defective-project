def change_zero_last_bits(bits, num_of_bits):
    bits_list = list(format(bits,b))
    for i in reserved(range(num_of_bits)):
        bits_list[len(bits_list)-i] = '0'

    return int("".join(bits_list))

# hint: 2進数表記にしたとき、第2引数で渡された桁から最初の桁までを0で埋める.
