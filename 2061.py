
def tong():
    u = n - 2
    v = m - 2
    sum = 0
    for i in range(u):
        for j in range(v):
            for x1 in range(3):
                for x2 in range(3):
                    sum += x[i + x1][j + x2] * h[x1][x2]
    return sum


t = int(input())
for _  in range(t):
    n, m = map(int, input().split())
    x = [] * n
    h = [] * 3
    for i in range(n):
        a = list(map(int, input().split()))
        x.append(a)
    for i in range(3):
        a = list(map(int, input().split()))
        h.append(a)
    print(tong())