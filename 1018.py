p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True:
    str = input()
    if str == '0':
        break
    k, s = str.split()
    k = int(k)
    res = ''
    for i in s:
        a = p.find(i)
        res = p[(a + k) % 28] + res
    print(res)