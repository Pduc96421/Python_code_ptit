from math import * 

def solve(n, k):
    ans = ""
    while n != 0:
        so = 0
        for i in range(0, k, 1):
            a = n % 10
            if a == 1:
                so += 2 ** i
            n //= 10
        if so >= 10:
            ans += str(chr(55 + so))
        else:
            ans += str(so)
    print(''.join(reversed(ans)))

if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        k = int(input())
        n = int(input())
        if k == 8:
            k = 3
        elif k == 16:
            k = 4
        elif k == 4:
            k = 2
        else:
            k = 1
        solve(n, k)