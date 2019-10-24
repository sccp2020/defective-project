def change_zero_last_bits(bits, num_of_bits):
    bits_list = list(str(bits))
    for i in range(num_of_bits):
        bits_list[-(i+1)] = '0'

    return int("".join(bits_list))

# hint: bitsとして渡された数字と、num_of_bits桁分の0の論理積をとります。
