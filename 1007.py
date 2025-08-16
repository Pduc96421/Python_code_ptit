
t = int(input())
for _ in range(t):
    n, x, m = map(float, input().split())
    ans = 0
    while n < m:
        n = n * (100 + x) * 0.01
        ans += 1
    print(ans)
