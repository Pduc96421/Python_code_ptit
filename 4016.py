from datetime import datetime

class khachHang:
    def __init__(self, maKh, tenKh, soPhong, ngayNhan, ngayTra, dichVu) -> None:
        self.maKh = maKh
        self.tenKh = tenKh
        self.soPhong = soPhong
        self.ngayNhan = ngayNhan
        self.ngayTra = ngayTra
        self.dichVu = dichVu
        date_format = "%d/%m/%Y"
        begin = datetime.strptime(self.ngayNhan, date_format)
        end = datetime.strptime(self.ngayTra, date_format)
        time = end - begin
        self.songay = time.days + 1

    def tongTien(self):
        tang = self.soPhong[0]
        gia = 0
        if tang == '1':
            gia = 25
        elif tang == '2':
            gia = 34 
        elif tang == '3':
            gia = 50
        else:
            gia = 80
        return gia * self.songay + self.dichVu
    
    def __str__(self) -> str:
        return '{} {} {} {} {}'.format(self.maKh, self.tenKh, self.soPhong, self.songay, self.tongTien())

t = int(input())
kh = []
for i in range(t):
    maKh = "KH" + format(i + 1, '02d')
    a = khachHang(maKh, input().strip(), input().strip(), input().strip(), input().strip(), int(input().strip()))
    kh.append(a)
kh.sort(key = lambda x : -x.tongTien())
for x in kh:
    print(x)