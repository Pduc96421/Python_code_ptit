

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def snt_cung_nhau(a, b):
    if gcd(a, b) == 1:
        return True
    else:
        return False 


n, k = map(int, input().split())
cnt = 0
for i in range(pow(10, k - 1) ,pow(10, k)):
    if snt_cung_nhau(n, i):
        cnt += 1
        print(i, end = ' ')
    if cnt == 10:
        cnt = 0
        print()