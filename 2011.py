n = int(input())
a = list(map(int, input().split()))
ans = 10**9
res = 0
for i in a:
    cnt = 0
    for j in a:
        cnt += abs(i - j)
    if cnt < ans:
        ans = cnt
        p = i
print(ans, p, sep=" ")