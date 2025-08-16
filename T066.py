
def xoay(a, b):
    if(len(a) != len(b)):
        return -1
    s = a
    for i in range(0, len(a) + 1):
        if s == b:
            return i
        s = s[1 : : ] + s[0]
    return -1


def sobuoc(a): 
    ans = 1000000
    for i in a:
        cnt = 0
        for j in a:
            tmp = xoay(j, i)
            if tmp == -1:
                return -1
            cnt += tmp
        ans = min(ans, cnt)
    return ans
        
# def sobuoc(a):
#     for i in range(0, len(a)):
#         a[i] = a[i][1 : :] + a[i][0]
#     return a

n = int(input())
a = []
for _ in range(n):
    a.append(input())
print(sobuoc(a))
