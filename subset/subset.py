def subset(ar, n):
    # Bug: reverse sorting breaks counting of duplicates
    res = 0
    ar.sort(reverse=True)
    for i in range(0, n):
        count = 1
        for i in range(n - 1):
            if ar[i] == ar[i + 1]:
                count+=1
            else:
                break
        res = max(res, count)
    return res
