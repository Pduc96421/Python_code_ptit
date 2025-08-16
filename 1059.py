
t = int(input())
for _ in range(t):
    n = input()
    tich = 1
    tong = 0
    cnt = 0
    for i in range(len(n)):
        if i % 2 == 0:
            tong += int(n[i])
        else:
            if n[i] != '0':
                cnt += 1
                tich *= int(n[i])
    if cnt == 0:
        tich = 0
    print(tong, tich, sep = " ")