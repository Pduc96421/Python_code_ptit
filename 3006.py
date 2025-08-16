from collections import Counter
import re

def tanxuat(s):
    word = re.findall(r'\b\w+\b', s.lower())
    dem_tu = Counter(word);
    dem_tu = sorted(dem_tu.items, key= lambda x : (-x[1], x[0]))
    return dem_tu

n = int(input())
s = ""
for _ in range(n):
    text = input()
    s += text + " "

for word, freq in tanxuat(s):
    pass