

t = int(input())
for _ in range(t):
    n = int(input())
    p = 1001
    thuong = [0] * p
    for i in range(n):
        x = int(input())
        thuong[x] += 1
    Max = max(thuong)
    for i in range(p):
        if thuong[i] == Max:
            print(i)
            break