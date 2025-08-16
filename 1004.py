from math import*

def snt(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, isqrt(n) + 1, 1):
        if n % i == 0:
            return False
    return True

def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)

t = int(input())
for i in range(t):
    n = int(input())
    cnt = 0;
    for i in range(n):
        if ucln(i, n) == 1:
            cnt += 1
    if snt(cnt):
        print('YES')
    else:
        print('NO')