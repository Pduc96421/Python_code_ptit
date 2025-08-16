from math import* 

def snt(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n >= 2

t = int(input())
for _ in range(t):
    n = input()
    cnt = 0
    for i in n:
        if i in ['2', '3', '5', '7']:
            cnt += 1
        else:
            cnt -= 1
    if snt(len(n)) and cnt > 0:
        print("YES")
    else:
        print("NO")