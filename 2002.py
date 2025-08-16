fib = [0] * 94

def fibonaci():
    fib[1] = 1
    fib[2] = 1
    for i in range(3, 94):
        fib[i] = fib[i - 1] + fib[i - 2]

fibonaci();
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        print(fib[i], end = " ")
    print()