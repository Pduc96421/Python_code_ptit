
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


t = int(input())
for _ in range(t):
    n = input()
    a = ''
    for i in n:
        a = i + a
    if gcd(int(n), int(a)) == 1:
        print("YES")
    else:
        print("NO")