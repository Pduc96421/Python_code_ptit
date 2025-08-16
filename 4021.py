
class gameThu:
    def __init__(self, maNc, tenNc, giovao, giora) -> None:
        self.maNc = maNc
        self.tenNc = tenNc
        self.giovao = giovao
        self.giora = giora

    def soPhut(self):
        x = int(self.giovao[:2]) * 60 + int(self.giovao[3:])
        y = int(self.giora[:2]) * 60 + int(self.giora[3:])
        return y - x
    
    def thoiGian(self):
        tong = self.soPhut()
        gio = tong // 60
        phut = tong - gio * 60
        return str(gio) + " gio " + str(phut) + " phut "
    
    def __str__(self) -> str:
        return '{} {} {}'.format(self.maNc, self.tenNc, self.thoiGian())

t = int(input())
gt = []
for i in range(t):
    maNc = input()
    tenNc = input()
    giovao = input()
    giora = input()
    a = gameThu(maNc, tenNc, giovao, giora)
    gt.append(a)
gt.sort(key = lambda x : -x.soPhut())
for x in gt:
    print(x)