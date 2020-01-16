# Given an tree as T, Should return max depth of T.
# FYI: if T is [1, 2, 3, 4, 5, 6, None, 8], it is this tree
#       ___________________________________
#      |            1                      |
#      |           / \                     |
#      |          /   \                    |
#      |         2     3                   |
#      |        / \   /                    |
#      |       4   5 6  (None so nothing)  |
#      |      /                            |
#      |     8                             |
#       ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
#      So, max_depth_binary_tree(T) is 4. (coz count(1-2-4-8))

def max_depth_binary_tree(T):
    i = len(T)-1
    count = 0
    depth = 1
    x = 2
    numN = 0
    while(i > count):
        if(T[count] == 'None'):
            numN += 1

        if(count == 0 and i > 1):
            depth += 1
        elif(count % x == 0):
            x = x * 2 - numN * 2
            depth += 1 
            numN = 0
        count += 1
        
    return depth
