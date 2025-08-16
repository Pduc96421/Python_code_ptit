
t = int(input())
for i in range(t):
    s = input()
    ok = True
    for i in range(0, len(s) - 1, 1):
        if s[i] > s[i + 1]:
            ok = False
            break;
    if ok:
        print("YES")
    else:
        print("NO")
