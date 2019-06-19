class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print(F"x: {self.x}, y: {self.y}")

    val = True


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(F"My name is: {self.name}")


point1 = Point(10, 20)
point1.draw()
if point1.val:
    print("Value is true")

# test person class
pers = Person("Mike")
pers.talk()
exit(0)
