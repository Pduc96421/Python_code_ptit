def check(n):
    for i in range(0, len(n), 2):
        if n[0] != n[i]:
            return False
    return True

t = int(input())
for _ in range(t):
    n = input()
    if len(n) % 2 != 0 and n[0] != n[1] and check(n):
        print("YES")
    else:
        print("NO")
