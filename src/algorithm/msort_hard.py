# Implement merge sort.
# You can not use loop

# merge([1, 5, 4], [2, 6, 3]) =>
# 1 : [5, 4], 2 : [6, 3]
# 1 < 2
# [1, merge([5, 4], [2, 6, 3])]
# [1] + 5: [4], 2: [6, 3]
# 5 > 2
# [1] + [2, merge([5, 4], [6, 3])
# [1] + [2, 5, 4, 6, 3]
# [1, 2, 5, 4, 6, 3]

def merge(arr1, arr2) :
    arr = []
    while len(arr1) > 0 and len(arr2) > 0 :
        if arr1[0] < arr2[0] :
            arr.append(arr1.pop(0))
        else :
            arr.append(arr2.pop(0))
    if len(arr1) != 0 :
        arr.extend(arr1)
    elif len(arr2) != 0 :
        arr.extend(arr2)
    return arr

def msort(arr, left = -1, right = -1) :
    if left == -1 : left, right = 0, len(arr)
    if left+1 < right :
        mid = (left + right) // 2
        msort(arr, left, mid)
        msort(arr, mid, right)
        arr[left : right] = merge(arr[left : mid], arr[mid : right])
    return arr
