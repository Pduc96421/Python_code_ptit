
class thiSinh:
    def __init__(self, maTs, tenTs, diemlt, diemth) -> None:
        self.maTs = maTs
        self.tenTs = tenTs
        self.diemlt = diemlt
        self.diemth = diemth

    def diemtb(self):
        return (self.diemth + self.diemlt) / 2
    
    def xeploai(self):
        dtb = self.diemtb()
        if dtb >= 9.5:
            return ('XUAT SAC')
        elif dtb >= 8.0:
            return ('DAT')
        elif dtb >= 5.0:
            return ('CAN NHAC')
        else:
            return ('TRUOT')
        
    def __str__(self) -> str:
        return '{} {} {:.2f} {}'.format(self.maTs, self.tenTs, self.diemtb(), self.xeploai())

t = int(input())
ts = []
for i in range(t):
    maTs = "TS0" + str(i + 1) 
    tenTs = input()
    diemlt = (lambda x : x if x <= 10 else x / 10.0)(float(input()))
    diemth = (lambda x : x if x <= 10 else x / 10.0)(float(input()))
    a = thiSinh(maTs, tenTs, diemlt, diemth)
    ts.append(a)
ts.sort(key = lambda x : -x.diemtb())
for x in ts:
    print(x)