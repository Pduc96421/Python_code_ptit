from itertools import combinations

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    comb = combinations(a, 3)
    ans = 3 * 10**8 + 1
    for i in comb:
        cnt = 0
        for j in i:
            cnt += j
        ans = min(ans, cnt)
    print(ans)