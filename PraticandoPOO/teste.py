import random

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        return self.x, self.y

    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        return f'({self.x}, {self.y})'

    # x + y ==> (2, 3) + (2, 2) => (4, 5)
    # x + 8 ==> (2, 3) + 8 => (10, 11)

    def __add__(self, other):
        if type(other) == Point:
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)

    #conceito de herança

class MyList(list):
    def choice(self):
        return random.choice(self)