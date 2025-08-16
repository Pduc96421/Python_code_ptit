x = []
t = int(input())
for _ in range(t):
    n = input()
    if n not in x:
        x.append(n)
print(len(x))