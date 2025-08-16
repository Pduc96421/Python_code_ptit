from math import*

def snt(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

def check(n):
    cnt = 0
    for i in n:
        if int(i) in [2, 3, 5, 7]:
            cnt += 1
        else:
            cnt -= 1
    if cnt > 0:
        return True
    else:
        return False

t = int(input())
for _ in range(t):
    n = input()
    if check(n) and snt(len(n)):
        print("YES")
    else:
        print("NO")