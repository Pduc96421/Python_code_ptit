from math import*

def tong(n):
    sum = 0
    while n != 0:
        a = n % 10
        if snt(a) == False:
            return False
        sum += a
        n //= 10
    if snt(sum) == False:
        return False
    return True

def dx(n):
    sum = 0
    while n != 0:
        a = n % 10
        sum = sum * 10 + a
        n //= 10
    return sum

def snt(n):
    if n == 0 and n == 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


t = int(input())
for _ in range(t):
    n = int(input())
    a = dx(n)
    if snt(n) and snt(a) and tong(n):
        print("Yes")
    else:
        print("No")