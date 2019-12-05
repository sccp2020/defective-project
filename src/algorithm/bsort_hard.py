# Implement buddle sort.
# You can not use loop

# bswap
# [4, 3, 1, (5), (2)] => swap 5, 2
# [4, 3, (1), (2), 5] => no swap
# [4, (3), (1), 2, 5] => swap 3, 1
# [(4), (1), 3, 2, 5] => swap 4, 1
# [(1), 4, 3, 2, 5]   => Left end is minimum value
def swap(arr, a, b) : arr[a], arr[b] = arr[b], arr[a]

def bswap(arr):
    n = len(arr)
    for i in range(n) :
        if(n-i-2 >= 0 and arr[n-i-2] > arr[n-i-1]) : swap(arr, n-i-2, n-i-1)
    return arr

def bsort(arr):
    for i in range(len(arr)) :
        bswap(arr)
    return arr
