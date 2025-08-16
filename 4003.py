from math import*

class phanSo:
    def __init__(self, tu, mau) -> None:
        self.tu = tu
        self.mau = mau
    def rutgon(self):
        mc = gcd(self.tu, self.mau)
        self.tu = self.tu // mc
        self.mau = self.mau // mc
    def __str__(self) -> str:
        self.rutgon()
        return '{}/{}'.format(self.tu, self.mau)

a, b = map(int, input().split())
ps = phanSo(a, b)
print(ps)