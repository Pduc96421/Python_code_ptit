from math import*

snt = [True] * 1004

def check():
    snt[0], snt[1] = False, False
    for i in range(2, isqrt(1004) + 1):
        if snt[i]:
            for j in range(i * i, 1004, i):
                snt[j] = False;

check()
n, m = map(int, input().split())
a = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
for i in range(n):
    for j in range(m):
        if snt[a[i][j]]:
            print(1, end = " ")
        else: 
            print(0, end = " ")
    print()