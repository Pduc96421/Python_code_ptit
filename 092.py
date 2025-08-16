
class sinhVien:
    def __init__(self, maSv, tenSv, diem, dantoc, khuvuc) -> None:
        self.maSv = "TS" + format(maSv, '02d')
        self.tenSv = tenSv
        self.diem = diem
        self.dantoc = dantoc
        self.khuvuc = khuvuc
    
    def chuanHoa(self):
        return ' '.join(i.capitalize() for i in self.tenSv.strip().split())
    
    def tongdiem(self):
        uutien = 0.0
        if self.dantoc != "Kinh":
            uutien += 1.5
        if self.khuvuc == 1:
            uutien += 1.5
        elif self.khuvuc == 2:
            uutien += 1.0
        else:
            uutien += 0.0    
        return self.diem + uutien
    
    def trangthai(self):
        if self.tongdiem() >= 20.5:
            return ('Do')
        else:
            return ('Truot')
        
    def __str__(self) -> str:
        return '{} {} {:.1f} {}'.format(self.maSv, self.chuanHoa(), self.tongdiem(), self.trangthai())

t = int(input())
sv = []
for i in range(t):
    a = sinhVien(i + 1, input(), float(input()), input(), int(input()))
    sv.append(a)
sv.sort(key = lambda x : (-x.tongdiem(), x.maSv))
for x in sv:
    print(x)