def findmin(a):
    if (len(a) == 1): return a
    else:
        if (a[0] < a[-1]): return findmin(a[:-1])
        else: return findmin(a[1:])

print(findmin([1,2,3]))
