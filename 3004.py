from collections import Counter
import re

def tan_xuat(text):
    word = re.findall(r'\b\w+\b', text.lower())
    dem_tu = Counter(word)
    dem_tu = sorted(dem_tu.items(), key = lambda x : (-x[1], x[0]))
    return dem_tu

t, k = map(int, input().split())
s = ""
for _ in range(t):
    text = input()
    s += text + " "

for word, freq in tan_xuat(s):
    if freq >= k:
        print(f'{word} {freq}')