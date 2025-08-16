from math import*

ham = [0] * (10 ** 8 + 1)

def check(n):
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    while n % 5 == 0:
        n //= 5
    return n == 1

def hamming():
    cnt = 1
    ham[1] = cnt
    for i in range(2, 10 ** 8 + 1):
        if check(i):
            cnt += 1
            ham[i] = cnt

hamming()
t = int(input())
for _ in range(t):
    n = int(input())
    if ham[n] == 0:
        print("Not in sequence")
    else:
        print(ham[n])