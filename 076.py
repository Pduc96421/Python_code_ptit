

d = dict()
class phim:
    def __init__(self, maPhim, matheloai, ngayshow, tenPhim, sotap) -> None:
        self.maPhim = maPhim
        self.matheloai = matheloai
        self.tenPhim = tenPhim
        self.ngayshow = ngayshow
        self.sotap = sotap
    
    def ngay(self):
        ans = ""
        x = self.ngayshow.split('/')
        ans += x[2]
        ans += x[1]
        ans += x[0]
        return ans
    
    def theloai(self):
        x = int(self.matheloai[2:])
        return d[x]
    
    def __str__(self) -> str:
        return "{} {} {} {} {}".format(self.maPhim, self.theloai(), self.ngayshow, self.tenPhim, self.sotap)

n, m = map(int, input().split())

for i in range(n):
    d[i + 1] = input().strip()

P = []
for i in range(m):
    a = phim("P" + format(i + 1, '03d'), input(), input(), input(),int(input().strip()))
    P.append(a)
P.sort(key = lambda x : (x.ngay(), x.tenPhim, -x.sotap))
for x in P:
    print(x)