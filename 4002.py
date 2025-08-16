
class Rectangle:
    def __init__(self, dai, rong, color)-> None:
        self.dai = dai
        self.rong = rong
        self.color = color.capitalize()
        self.area = self.dai * self.rong
        self.perimeter = (self.dai + self.rong) * 2
    def __str__(self) -> str:
        if self.dai > 0 and self.rong > 0:
            return '{} {} {}'.format(self.perimeter, self.area, self.color)
        else:
            return ('INVALID')


a = input().split()
rec = Rectangle(int(a[0]), int(a[1]), (a[2]))
print(rec)