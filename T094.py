
d = dict()

class nhanVien:
    def __init__(self, manv, tennv, luongcb, soNgay):
        self.manv = manv
        self.tennv = tennv
        self.luongcb = luongcb
        self.soNgay = soNgay
        nhom = self.manv[0]
        nam = int(self.manv[1: 3: ])
        if 1 <= nam <= 3:
            if nhom == 'A' or nhom == 'B':
                self.heso = 10
            elif nhom == 'C':
                self.heso = 9
            else:
                self.heso = 8

        elif 4 <= nam <= 8:
            if nhom == 'A':
                self.heso = 12
            elif nhom == 'B':
                self.heso = 11
            elif nhom == 'C':
                self.heso = 10
            else:
                self.heso = 9

        elif 9 <= nam <= 15:
            if nhom == 'A':
                self.heso = 14
            elif nhom == 'B':
                self.heso = 13
            elif nhom == 'C':
                self.heso = 12
            else:
                self.heso = 11

        elif nam >= 16:
            if nhom == 'A':
                self.heso = 20
            elif nhom == 'B':
                self.heso = 16
            elif nhom == 'C':
                self.heso = 14
            else:
                self.heso = 13

        self.tongluong = self.luongcb * self.soNgay * self.heso * 1000

    def __str__(self):
        return f"{self.manv} {self.tennv} {d[self.manv[3:]]} {self.tongluong}"
    
n = int(input())
for _ in range(n):
    s = list(input().split())
    b = s[1:]
    d[s[0]] = ' '.join(b)

m = int(input())
nv = []
for _ in range(m):
    nv.append(nhanVien(input(), input(), int(input()), int(input())))

for x in nv:
    print(x)