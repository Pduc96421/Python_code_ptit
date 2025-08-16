a = [1] * 10001
prime = []

def sieve():
    a[0] = 0
    a[1] = 0
    for i in range(2, 10001):
        if a[i] == 1:
            for j in range(i * i, 10001, i):
                a[j] = 0
            prime.append(i)

sieve()
n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in l:
    tmp = 10 ** 9
    for j in prime:
        tmp = min(tmp, abs(j - i))
    ans = max(ans, tmp)
print(ans)