
def dao(n):
    ans = 0
    while n != 0:
        a = n % 10
        ans = ans * 10 + a
        n //= 10
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    ok = True
    for _ in range(1000):
        a = dao(n) + n
        if n % 7 == 0:
            ok = False
            print(n)
            break
        if a % 7 == 0:
            ok = False
            print(a)
            break
        n = a
    if ok:
        print("-1")