n = int(input())
a = []
for _ in range(n):
    a.append(input())
i = 0
ans = []
while i < n - 1:
    x = list(map(str, a[i].split())) 
    if len(x) == 7:
        ans.append(2)
        i += 4
    else:
        ans.append(1)
        while len(x) != 7 and i < n - 1:
            x = list(map(str, a[i].split())) 
            i += 1
print(len(ans))
for i in ans:
    print(i)