# count_str:
# count each characters
#  e.g, s="aaabbbc", then this func return {"a":3, "b":2, "c":1}

def count_str(s):
    counter = {}
    for c in s:
        if not c in counter:
            counter[c] = 1
        else:
            counter[c] +=1
    return counter
