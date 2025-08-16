class thiSinh:
    def __init__(self, tenTs, bd, x1, x2, x3) -> None:
        self.tenTs = tenTs
        self.bd = bd
        self.tongDiem = x1 + x2 + x3
    def __str__(self) -> str:
        return '{} {} {:.1f}'.format(self.tenTs, self.bd, self.tongDiem)

a = thiSinh(input(), input(), float(input()), float(input()), float(input()))
print(a)