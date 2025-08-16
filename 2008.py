from math import*

p = [1] * 10001

def snt():
    p[0] = p[1] = 0
    for i in range(isqrt(10001)):
        if p[i]:
            for j in range(i * i, 10001, i):
                p[j] = 0

snt()
n, x = map(int, input().split())
i = 0
cnt = 0
while cnt <= n:
    if p[i]:
        print(x, end = " ")
        x += i
        cnt += 1
    i += 1
    