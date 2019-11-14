# Implement insertion sort.
# You can not use loop

# insert(3, [1, 2, 4, 5]) -> [1, 2, 3, 4, 5] 
def insert(x, arr):
    if x<=0:
        return(arr)
    for i in range(len(arr)-x):
        if arr[i]>arr[len(arr)-x]:
            a=arr[len(arr)-x]
            del arr[len(arr)-x]
            arr.insert(i,a)

    return insert(x-1,arr)

def isort(arr):
    return insert(len(arr),arr)
