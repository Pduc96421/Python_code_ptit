s = input()
low, up = 0, 0
for i in s:
    if i.islower():
        low += 1
    else:
        up += 1
if(low >= up):
    print(s.lower())
else:
    print(s.upper())