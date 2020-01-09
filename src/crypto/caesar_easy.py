# clartext: string, key: number
# Plase encrypto alphabet. Keep symbol.


def caesar(cleartext, key):
    result = ''
    for c in cleartext:
        if 'A' <= c and c <= 'Z':
            result += chr((ord(c) - ord('A') + key) % 26 + ord('A'))
        elif 'a' <= c and c <= 'z':
            result += chr((ord(c) - ord('a') + key) % 26 + ord('a'))
        else:
            result += c

    return(result)
