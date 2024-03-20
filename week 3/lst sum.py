def calcTotal(lst):
    total = 0
    for v in lst:
        total += v
    return total

lst = [1,2,3,4]

n = calcTotal(lst)

print(n)