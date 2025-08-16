
def tong(n):
    sum = 0
    while n != 0:
        a = n % 10
        sum += a
        n //= 10
    if sum % 10 == 0:
        return True
    else:
        return False

def distance(n):
    a = str(n)
    for i in range(len(a) - 1):
        b = ord(a[i])
        c = ord(a[i + 1])
        if abs(b - c) != 2:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    if tong(n) and distance(n):
        print("YES")
    else:
        print("NO")