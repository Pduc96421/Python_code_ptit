from math import*

se = set({})
while True:
    try:
        s = list(map(int, input().split()))
        for i in s:
            se.add(i % 42)
    except EOFError:
        break
print(len(se))