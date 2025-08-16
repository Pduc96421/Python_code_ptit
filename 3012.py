class Sinh_vien:
    def __init__(self, hoten, accepted, submit):
        self.hoten = hoten
        self.accepted = accepted
        self.submit = submit
    def __str__(self):
        return f"{self.hoten} {self.accepted} {self.submit}"
    
t = int(input())
sv = []
for _ in range(t):
    hoten = input()
    a, s = map(int, input().split())
    sv.append(Sinh_vien(hoten, a, s))
sv.sort(key = lambda x : (-x.accepted, x.submit, x.hoten))
for x in sv:
    print(x)