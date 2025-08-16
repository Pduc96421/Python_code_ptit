t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    se = set()
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        se.add(i)
    ok = False
    for i in se:
        if d[i] > n / 2:
            print(i)
            ok = True
            break
    if ok == False:
        print("NO")