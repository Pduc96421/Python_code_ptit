n = int(input())
a = list(map(float, input().split()))
Max = max(a)
Min = min(a)
cnt = 0
sum = 0
for i in a:
    if i != Max and i != Min:
        cnt += 1
        sum += i
print('{:.2f}'.format(sum / cnt))