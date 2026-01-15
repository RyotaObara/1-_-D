# 課題D-3: 正方形オブジェクト
import math

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        # 面積 = 一辺 × 一辺
        result = self.side ** 2
        return f"{result:.2f}"

    def diagonal(self):
        # 対角線 = sqrt(side^2 + side^2)
        result = math.hypot(self.side, self.side)
        return f"{result:.2f}"

# 計算

square1 = Square(side=1.5)
print(square1.area())
print(square1.diagonal())

square2 = Square(side=15)
print(square2.area())
print(square2.diagonal())
