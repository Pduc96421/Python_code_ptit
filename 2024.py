from functools import cmp_to_key

def mul(a):
    ans = 1
    for i in str(a):
        ans *= int(i)
    return ans

def cmp(a, b):
    if mul(a) != mul(b):
        if mul(a) > mul(b):
            return 1
        else: 
            return -1
    else:
        if a > b:
            return 1
        else:
            return -1


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = cmp_to_key(cmp))
    for i in a:
        print(i , end = " ")
    print()