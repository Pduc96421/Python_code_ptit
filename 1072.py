
n, k = map(int, input().split())
s = set(map(int, input().split()))
a = list(s)
a.sort()
x = [0] * (len(a) + 1)

def inkq():
    for i in range(1, k + 1, 1):
        print(a[x[i] - 1], end = " ")
    print()

def Try(i):
    for j in range(x[i - 1] + 1, len(a) - k + i + 1):
        x[i] = j
        if i == k:
            inkq()
        else:
            Try(i + 1)
            
Try(1)
