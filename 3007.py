from sys import stdin

s = ""
for line in stdin:
    a = line.strip().split()
    for x in a:
        s += x + " "
s = s.lower()
s = s.replace('?', '.')
s = s.replace('!', '.')
s = s.replace(". ", ".")
s = s.replace(" . ", ".")
s = s.replace(" .", ".")
ans = s.split('.')
for x in ans:
    print(x.capitalize())
