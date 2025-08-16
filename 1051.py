t = int(input())
for _ in range(t):
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    tmp = str(sum)
    dao = tmp[: : -1]
    if dao == tmp and len(tmp) > 1:
        print("YES")
    else:
        print("NO")