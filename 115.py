
def ans(n):
    sum = 0
    while n != 0:
        a = n % 10
        sum += giai_thua(a)
        n //= 10
    return sum

def giai_thua(n):
    tich = 1
    for i in range(1, n + 1):
        tich *= i
    return tich

t = int(input())
for _ in range(t):
    n = int(input())
    a = ans(n)
    if n == a:
        print('Yes')
    else:
        print('No')