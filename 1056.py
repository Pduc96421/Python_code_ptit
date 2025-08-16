from math import*

def snt(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
        if i % 2 == 0:
            if int(n[i]) % 2 != 0:
                return False
        else:
            if int(n[i]) % 2 == 0:
                return 
    if snt(sum) == False:
        return False
    return True

t = int(input())
for _ in range(t):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")