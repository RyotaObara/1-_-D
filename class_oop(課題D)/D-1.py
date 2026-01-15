# 課題D-1: 円オブジェクト
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    # 面積 = π * r^2
    def area(self):
        return round(math.pi * (self.radius**2), 2)

    # 周囲長 = 2 * π * r
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)


circle1 = Circle(radius=1)
print(circle1.area())
print(circle1.perimeter())

circle3 = Circle(radius=3)
print(circle3.area())
print(circle3.perimeter())


