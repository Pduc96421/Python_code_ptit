a, k, n = map(int, input().split())
begin = k - (a % k)
end = n - a;
if begin > end:
    print('-1')
else:
    for i in range(begin, end + 1, k):
        print(i, end = ' ')