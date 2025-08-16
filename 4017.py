
class thiSinh:
    def __init__(self, tenTs, quequan, candich) -> None:
        self.tenTs = tenTs
        self.quequan = quequan
        self.id = ''.join(i[0] for i in quequan.split() + tenTs.split())
        h, m = map(int, candich.split(':'))
        self.V = (120 / (h - 6 + m / 60))

    def __str__(self) -> str:
        return "{} {} {} {} Km/h".format(self.id, self.tenTs, self.quequan, round(self.V)) 

t = int(input())
ts = []
for i in range(t):
    a = thiSinh(input(), input(), input())
    ts.append(a)
ts.sort(key = lambda x : -x.V)
for x in ts:
    print(x)