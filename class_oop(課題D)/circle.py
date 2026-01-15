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


# 課題D-2: 長方形オブジェクト
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # 面積 (縦 × 横)
    def area(self):
        res = self.height * self.width
        return f"{res:.2f}"

    # 対角線 (√(縦^2 + 横^2))
    def diagonal(self):
        # ** 0.5 でルート（平方根）を計算
        res = (self.height**2 + self.width**2) ** 0.5
        return f"{res:.2f}"


#
rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())
print(rectangle1.diagonal())

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())
print(rectangle2.diagonal())



# 課題D-3: 正方形オブジェクト
class Square:
    def __init__(self, side):
        self.side = side

    # 面積 (一辺 × 一辺)
    def area(self):
        res = self.side**2
        return int(res) if res.is_integer() else res

    # 対角線 (√(side^2 + side^2))
    def diagonal(self):
        # 三平方の定理: side * √2
        res = (self.side**2 + self.side**2) ** 0.5
        return f"{res:.2f}"


# 計算
square1 = Square(side=1.5)
print(square1.area())
print(square1.diagonal())

square2 = Square(side=15)
print(square2.area())
print(square2.diagonal())


# 課題D-4: カウンターその1
class MyCounterV1:
    def __init__(self, value):
        self.value = value

    def count_up(self):
        self.value += 1


# 計算

# counter1
counter1 = MyCounterV1(value=0)
print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2

# counter2
counter2 = MyCounterV1(value=7)
print(counter2.value)  # 7

counter2.count_up()
print(counter2.value)  # 8

counter2.count_up()
print(counter2.value)  # 9

# 課題D-5: カウンターその2
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # 面積 = πr^2
        return f"{math.pi * self.radius**2:.2f}"

    def perimeter(self):
        # 周囲長 = 2πr
        return f"{2 * math.pi * self.radius:.2f}"


# 課題D-6: カウンターその3
class MyCounterV3:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value += self.step

    def count_down(self):
        self.value -= self.step


# 実行
counter1 = MyCounterV3(value=1, step=2)
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 3 (1 + 2)

counter1.count_up()
print(counter1.value)  # 5 (3 + 2)

counter1.count_down()
print(counter1.value)  # 3 (5 - 2)

counter2 = MyCounterV3(value=3, step=4)
print(counter2.value)  # 3

counter2.count_down()
print(counter2.value)  # -1 (3 - 4)

counter2.count_down()
print(counter2.value)  # -5 (-1 - 4)
