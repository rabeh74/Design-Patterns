"""
1- Composite is a structural design pattern that lets you compose objects into tree structures
and then work with these structures as if they were individual objects.
2- client code works with both simple and complex components through a common interface 
 """


from abc import ABC, abstractmethod
class Graphic(ABC):
    @abstractmethod
    def move(self, x, y):
        pass
    @abstractmethod
    def draw(self):
        pass
class Dot(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, x, y):
        self.x += x
        self.y += y
    def draw(self):
        print("Drawing dot at ({}, {})".format(self.x, self.y))
class Circle(Graphic):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    def move(self, x, y):
        self.x += x
        self.y += y
    def draw(self):
        print("Drawing circle at ({}, {}) with radius {}".format(self.x, self.y, self.radius))

class CompoundGraphic(Graphic):
    def __init__(self):
        self._children = []
    def add(self, child):
        self._children.append(child)
    def remove(self, child):
        self._children.remove(child)
    def move(self, x, y):
        for child in self._children:
            child.move(x, y)
    def draw(self):
        for child in self._children:
            child.draw()
def client_code(component):
    component.move(1, 1)
    component.draw()
if __name__ == "__main__":
    dot = Dot(1, 2)
    circle = Circle(5, 3, 10)
    client_code(dot)
    compound = CompoundGraphic()
    compound.add(dot)
    compound.add(circle)
    client_code(compound)

