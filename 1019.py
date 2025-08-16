t = int(input())
for _ in range(t):
    s = input()
    t = s[: : - 1]
    ok = True
    for i in range(len(s) - 1):
        a = abs(ord(s[i]) - ord(s[i + 1]))
        b = abs(ord(t[i]) - ord(t[i + 1]))
        if a != b:
            ok = False
            break;
    if ok :
        print("YES")
    else:
        print("NO")