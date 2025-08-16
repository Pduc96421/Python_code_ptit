from math import*

prime = [True] * 501

def snt():
    prime[0], prime[1] = False, False
    for i in range(isqrt(501)):
        if(prime[i]):
            for i in range(i * i, 501, i):
                prime[i] = False

def check(n):
    for i in range(len(n)):
        if prime[i] != prime[int(n[i])]:
            return False
    return True

snt()
t = int(input())
for _ in range(t):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")