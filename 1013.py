from math import*

def snt(n):
    for i in range(2, isqrt(n) + 1):
        if(n % i == 0):
            return False
    return n >= 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def check(n):
    sum = 0
    while n != 0:
        a = n % 10
        sum += a
        n //= 10
    return sum

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    n = gcd(a, b)
    if snt(check(n)):
        print('YES')
    else:
        print('NO')
