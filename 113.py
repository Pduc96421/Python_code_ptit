from math import*

def dx(n):
    sum = 0
    while n != 0:
        a = n % 10 
        sum = sum * 10 + a
        n //= 10
    return sum

def check(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    b = []
    for i in range(10, n):
        a = dx(i)
        if a != i and a < n:
            if check(a) and check(i) and (i not in b):
                b = b + [i] + [a]
    for i in b:
        print(i, end = ' ')
    print()