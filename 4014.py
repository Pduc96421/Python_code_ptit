def custom_round(number, decimal_places):
  factor = 10 ** decimal_places
  rounded_number = int(number * factor + 0.5) / factor
  return rounded_number

class bangDiem:
    def __init__(self, maHs, tenHs, diemTb) -> None:
        self.maHs = maHs
        self.tenHs = tenHs
        self.diemTb = custom_round(diemTb / 12, 1)
    
    def xeploai(self):
        if self.diemTb >= 9.0:
            return ('XUAT SAC')
        elif self.diemTb >= 8.0:
            return ('GIOI')
        elif self.diemTb >= 7.0:
            return ('KHA')
        elif self.diemTb >= 5.0:
            return ('TB')
        else:
            return('YEU')

    def __str__(self) -> str:
        return '{} {} {} {}'.format(self.maHs, self.tenHs, self.diemTb, self.xeploai())

t = int(input())
bd = []
for i in range(1, t + 1):
    maHs = "HS" + format(i, '02d')
    tenHs = input()
    diem = input().split()
    diem = [float(i) for i in diem]
    tongDiem = sum(diem) + diem[0] + diem[1]
    a = bangDiem(maHs, tenHs,  tongDiem)
    bd.append(a)
bd.sort(key = lambda x : -x.diemTb)
for x in bd:
    print(x)