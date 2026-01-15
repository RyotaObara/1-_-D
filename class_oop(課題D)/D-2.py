# 課題D-2: 長方形オブジェクト
import math

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        result = self.height * self.width
        return f"{result:.2f}"

    def diagonal(self):
        result = math.hypot(self.height, self.width)
        return f"{result:.2f}"

# 計算

rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())
print(rectangle1.diagonal())

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())
print(rectangle2.diagonal())
