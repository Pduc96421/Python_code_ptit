
n = int(input())
a = []
for i in range(n):
    a.append(input())
doc = [0] * n
ngang = [0] * n
for i in range(n):
    for j in range(n):
        if a[i][j] == 'C':
            doc[i] += 1
            ngang[j] += 1
ans = 0
for i in range(n):
    if doc[i] >= 2:
        ans += doc[i] * (doc[i] - 1) // 2
    if ngang[i] >= 2:
        ans += ngang[i] * (ngang[i] - 1) // 2
print(ans) 