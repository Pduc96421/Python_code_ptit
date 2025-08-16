t = int(input())
for _ in range(t):
    n = input()
    for i in range(0, len(n)):
        if n[i].isdigit():
            a = int(n[i])
            for j in range(a):
                print(n[i - 1], end = '')
    print()