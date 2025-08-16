from math import*

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
    ans = 0
    for i in range(n - 4):
        if (check(i) and check(i + 2) and check(i + 6)) or (check(i) and check(i + 4) and check(i + 6)):
            ans += 1
    print(ans)
