from math import*

def snt(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n >= 2

t =int(input())
for _ in range(t):
    s = input()
    n = int(s[-4 : : ])
    if snt(n):
        print("YES")
    else:
        print("NO")
