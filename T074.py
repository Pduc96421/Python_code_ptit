
n = int(input())
for _ in range(n):
    a = list(map(str, input().split()))
    ans = 0
    for i in a:
        if ans + len(i) <= 100:
            if len(i) + ans < 100:
                print(i, end = " ")
                ans += len(i) + 1
            else:
                print(i, end = "")
        else:
            break
    print()