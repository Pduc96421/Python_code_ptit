t = int(input())
for _ in range(t):
    n = input()
    tich = 1
    for i in n:
        if int(i) != 0:
            tich *= int(i)
    print(tich)