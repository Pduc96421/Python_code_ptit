from math import*


class phanSo():
    def __init__(self, tu, mau) -> None:
        self.tu = tu
        self.mau = mau
    def rutgon(self):
        mc = gcd(self.tu, self.mau)
        self.tu = self.tu // mc
        self.mau = self.mau // mc
    def tong(self, p):
        x = self.tu * p.mau + p.tu * self.mau
        y = self.mau * p.mau
        ans = phanSo(x, y)
        ans.rutgon()
        return ans
    def __str__(self) -> str:
        return '{}/{}'.format(self.tu, self.mau)

a, b, c, d = map(int , input().split())
x = phanSo(a, b)
y = phanSo(c, d)
print(x.tong(y))