
def check(n):
    for i in n:
        if int(i) % 2 != 0:
            return False
    if n != n[: : -1]:
        return False
    return len(a) % 2 == 0

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(22, n, 2):
        a = str(i)
        if check(a):
            print(i, end = ' ')
    print()