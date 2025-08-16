from math import*

def phan_tich(n):
    print("1 * ", end = '')
    for i in range(2, isqrt(n) + 1):
        cnt = 0
        if n % i == 0:
            while n % i == 0:
                cnt += 1
                n = n // i
            print(i, cnt, sep = "^", end = ' ')
            if n != 1:
                print("*", end = " ")
        
    if(n != 1):
        print(n, "^", 1, sep = '', end = '')

t = int(input())
for _ in range(t):
    n = int(input())
    phan_tich(n)
    print()
