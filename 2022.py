from math import*

def snt(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

n = int(input())
a = list(map(int, input().split()))
d = dict()
res = []
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
    if i not in res and snt(i):
        res.append(i)
for i in res:
    print(i, d[i], sep = ' ')