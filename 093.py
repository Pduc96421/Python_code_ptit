
from math import *

class sinhVien:
    def __init__(self, masv, tensv, mon1, mon2, mon3):
        self.masv = "SV" + format(masv, '02d')
        self.tensv = self.chuanhoa(tensv)
        self.diemtb = (mon1 * 3 + mon2 * 3 + mon3 * 2) / (3 + 3 + 2)
        pass

    def chuanhoa(self, hoten):
        return ' '.join(str(i).capitalize() for i in str(hoten).strip().split())
    
    def __str__(self):
        return '{:s} {:s} {:.2f} {:d}'.format(self.masv, self.tensv, ceil(self.diemtb * 100) / 100, self.xephang)
    
n = int(input())
sv = []
for t in range(n):
    sv.append(sinhVien(t + 1, input(), float(input()), float(input()), float(input())))

sv.sort(key = lambda x : (-x.diemtb, x.masv))

sv[0].xephang = 1
for i in range(1, len(sv)):
    if sv[i].diemtb == sv[i - 1].diemtb:
        sv[i].xephang = sv[i - 1].xephang
    else:
        sv[i].xephang = i + 1
    
for x in sv:
    print(x)