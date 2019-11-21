# Implement insertion sort.
# You can not use loop

# insert(3, [1, 2, 4, 5]) -> [1, 2, 3, 4, 5]

def insert(x,arr):
    for i in range(len(arr)):
        if (x <= arr[i]) :
            arr.insert(i,x)
            return arr
    arr.insert(len(arr),x)
    return arr    

def isort(arr):
    toarr=[]
    for i in range(len(arr)):
        toarr=insert(arr[i],toarr)
    return toarr
