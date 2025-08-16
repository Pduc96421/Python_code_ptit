from math import*

a = [0] * (10 ** 7 + 1)

def uoc_so(n):
    cnt = 0
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            cnt += 1
            if i != (n // i):
                cnt += 1
    return cnt

def solve(n):
    for i in range(1, n):
        if uoc_so(i) >= uoc_so(n):
           return False
    return True

def init():
    for i in range(1, 10 ** 7 + 1):
        if solve(i):
            a[i] = 1

init()
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n, 10 ** 7 + 1):
        if a[i] != 0:
            print(i)
            break
