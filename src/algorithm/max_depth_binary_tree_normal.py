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
    i = len(T)
    count = 0
    j = 1
    while(i >= j):
        j *= 2  
        count += 1
        
    return count
