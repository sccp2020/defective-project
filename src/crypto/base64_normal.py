# s: string
# 入力された文字列をバイナリの文字列に変換します
# e.g str2Bin("abcdefg") => "01100001011000100110001101100100011001010110011001100111"
def str2Bin(s):
    binList = list(map(ord, list(s)))
    return ''.join(map(lambda c: format(c, '08b'), binList))

# n: number, t: string
# 入力された文字列の右側をtで合計n文字になるようにする関数を生成します
# e.g fill(5, 'x')('a') => 'axxxx'
def fill(n, t):
    return lambda s: s.ljust(n, t)

# s: string, n: number
# sをn個ずつに分割します（足りなくてn個にならない場合もあります）
# e.g split("abcdefg", 3) => ["abc", "def", "g"]
def split(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

# b: string
# 入力されたバイナリ文字列を変換する表です
# e.g table('000111') => 'H'
def table(b):
    t = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
    return t[int(b, 2)]

# s: string
# 与えられた文字列をbase64エンコーディングします
# e.g base64("abcdefg") => "YWJjZGVmZw=="
def base64(s):
    # 上に与えられている関数を使ってbase64エンコーディングをする関数を完成させてください。
    # 参考 : https://ja.wikipedia.org/wiki/Base64
    return s

