def solve(p, q, X):
    New = X.replace(str(q), str(p))
    return int(New)

if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        p, q = map(int, input().split())
        a = list(input().split())
        if len(a) == 1:
            X1 = a[0]
            X2 = input()
        else:
            X1, X2 = a[0], a[1]

        a = solve(p, q, X1)
        b = solve(p, q, X2)

        c = solve(q, p, X1)
        d = solve(q, p, X2)

        sum1 = a + b
        sum2 = c + d
        print(min(sum1, sum2), max(sum1, sum2), sep = ' ', end = '\n')
