# clartext: string, key: number
# Plase encrypto alphabet. Keep symbol.


def caesar(cleartext, key):
    result = ''
    for c in cleartext:
        if 'A' <= c and c <= 'Z':
            result += chr((ord(c) - ord('A') + 1) % 26 + ord('A'))
        else:
            result += c

    return(result)
