from math import * 

class khachHang:
    def __init__(self, maKh, tenKh, soNuoc) -> None:
        self.tenKh = tenKh
        self.maKh = maKh
        self.soNuoc = soNuoc
    
    def tongTien(self):
        ans = 0
        if self.soNuoc <= 50:
            ans = self.soNuoc * 100 * 1.02
        elif self.soNuoc <= 100:
            ans = (50 * 100 + (self.soNuoc - 50) * 150) * 1.03
        else:
            ans = ((self.soNuoc - 100) * 200 + (50 * 100) + (50 * 150)) * 1.05
        return round(ans)
    def __str__(self) -> str:
        return '{} {} {}'.format(self.maKh, self.tenKh, self.tongTien())

t = int(input())
kh = []
for i in range(1, t + 1):
    maKh = "KH" + format(i, '02d')
    tenKh = input()
    soCu = int(input())
    soMoi = int(input())
    a = khachHang(maKh, tenKh, soMoi - soCu)
    kh.append(a)
kh.sort(key = lambda x : -x.tongTien())
for x in kh:
    print(x)