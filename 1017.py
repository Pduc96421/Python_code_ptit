t = int(input())
for _ in range(t):
    n = input()
    n = n + '@'
    cnt = 1
    for i in range(len(n) - 1):
        if n[i] == n[i + 1]:
            cnt += 1
        else:
            print(cnt, n[i], sep = '', end = '')
            cnt = 1
    print()