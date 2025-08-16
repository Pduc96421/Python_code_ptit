
t = int(input())
for _ in range(t):
    s = input()
    if len(s) < 3:
        print("NO")
    else:
        i = 0
        while ord(s[i]) < ord(s[i + 1]):
            i += 1
        ok = 1
        for i in range(i, len(s) - 1):
            if ord(s[i]) <= ord(s[i + 1]):
                ok = 0
                break
        if ok:
            print("YES")
        else:
            print("NO")
