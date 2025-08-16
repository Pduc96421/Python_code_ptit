
class danhba:
    def __init__(self, ten, ngay, sodt) -> None:
        self.ten = ten
        self.ngay = ngay
        self.sodt = sodt
    
    

file = open("SOTAY.txt", 'r')
a = []
for line in file:
    a.append(line.strip())

db = []
i = 0
while i < len(a):
    if a[i][:4:] == 'Ngay':
