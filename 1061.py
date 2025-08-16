from math import*

def snt(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

t = int(input())
for _ in range(t):
    n = input()
    a = int(n[: 3])
    b = int(n[-3 :])
    if snt(a) and snt(b):
        print("YES")
    else:
        print("NO")