
class sinhVien:
    def __init__(self, maSv, tenSv, lop) -> None:
        self.maSv = maSv
        self.tenSv = tenSv
        self.lop = lop
        self.data = ""
    
    def chuyencan(self):
        diem = 10
        for x in self.data:
            if x == 'v':
                diem -= 2
            elif x == 'm':
                diem -= 1
        if diem <= 0:
            return 0
        else:
            return diem
        
    def ghichu(self):
        if self.chuyencan() == 0:
            return ("KDDK")
        else:
            return("")
        
    def __str__(self) -> str:
        return '{} {} {} {} {}'.format(self.maSv, self.tenSv, self.lop,self.chuyencan(), self.ghichu())

t = int(input())
d = dict()
sv = []
for i in range(t):
    a = sinhVien(input(), input(), input())
    sv.append(a)
for i in range(t):
    a = input().split()
    d[a[0]] = a[1]
for x in sv:
    x.data = d[x.maSv]

for x in sv:
    print(x)
