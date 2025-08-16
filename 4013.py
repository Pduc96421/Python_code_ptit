
class tramDo:
    def __init__(self, maTram, tenTram) -> None:
        self.maTram = maTram
        self.tenTram = tenTram
        self.luongmua = 0
        self.giomua = 0.0
    def luongmauTb(self):
        return self.luongmua / self.giomua
    def __str__(self) -> str:
        return '{} {} {:.2f}'.format(self.maTram, self.tenTram, self.luongmauTb())

t = int(input())
s = set()
ans = []
id = 1
for _ in range(t):
    tenTram = input()
    batdau = input()
    ketthuc = input()
    luongMua = int(input())
    x = batdau.split(':')
    y = ketthuc.split(':')
    x1, x2, y1, y2 = int(x[0]), int(x[1]), int(y[0]), int(y[1])
    thoiGian = (60 * (y1 - x1) + (y2 - x2)) / 60.0
    if tenTram not in s:
        s.add(tenTram)
        maTram = "T" + format(id, '02d')
        id += 1
        a = tramDo(maTram, tenTram)
        a.luongmua += luongMua
        a.giomua += thoiGian
        ans.append(a)
    else:
        for i in range(len(ans)):
            if ans[i].tenTram == tenTram:
                ans[i].luongmua += luongMua
                ans[i].giomua += thoiGian
                break
for i in ans:
    print(i)