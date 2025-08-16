
class gianVien:
    def __init__(self, ma_Gv, ten_Gv, ma_xettuyen, diem_th, diem_cm) -> None:
        self.ma_Gv = ma_Gv
        self.ten_GV = ten_Gv
        self.ma_xettuyen = ma_xettuyen
        self.diem_th = diem_th
        self.diem_cm = diem_cm

    def tongDiem(self):
        diem = self.diem_th * 2 + self.diem_cm
        x = self.ma_xettuyen[1]
        if x == '1':
            diem += 2.0
        elif x == '2':
            diem += 1.5
        elif x == '3':
            diem += 1.0
        else:
            diem += 0.0
        return diem
    
    def monHoc(self):
        x = self.ma_xettuyen[0]
        if x == 'A':
            return ('TOAN')
        elif x == 'B':
            return ('LY')
        else:
            return ('HOA')

    def xeploai(self):
        if self.tongDiem() >= 18.0:
            return ('TRUNG TUYEN')
        else:
            return('LOAI')

    def __str__(self) -> str:
        return '{} {} {} {:.1   f} {}'.format(self.ma_Gv, self.ten_GV, self.monHoc(), self.tongDiem(), self.xeploai())

t = int(input())
gv = []
for i in range(t):
    a = gianVien("GV" + format(i + 1, '02d'), input(), input(), float(input()), float(input()))
    gv.append(a)
gv.sort(key = lambda x : -x.tongDiem())
for x in gv:
    print(x)