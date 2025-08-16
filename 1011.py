
def snt(n):
    x = str(n)
    l, r = 0, len(x) - 1
    while l < r:
        if x[l] != x[r]:
            return False
        l += 1
        r -= 1
    return True

def check(n):
    digit = ['0', '2', '4', '6', '8']
    x = str(n)
    for i in x:
        if i not in digit:
            return False
    return len(x) % 2 == 0 and snt(n)

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(22, n):
        if check(i):
            print(i, end = " ")
    print()