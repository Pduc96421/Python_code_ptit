t = int(input())
for _ in range(t):
    s = input()
    a = list(map(int, s))
    for i in range(len(a) - 1, 0, -1):
        if a[i] >= 5:
            a[i - 1] += 1
        a[i] = 0
        if a[0] == 0:
            a = [1] + a
    for i in a:
        print(i, end = '')
    print()
"""
7
15
14
5
99
12345678
44444445
1445
"""