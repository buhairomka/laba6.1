from abs import ABS, abstractmethod
import math


class triangle(ABS):
    @abstractmethod
    def __init__(self):
        self.side1 = 0
        self.side2 = 0
        self.angle = 0
        self.square = 0
        self.perimeter = 0

    @abstractmethod
    def sq(self):
        pass

    @abstractmethod
    def P(self):
        pass


class rightTriangle(triangle):
    def __init__(self):
#        super().__init__()
        self.side1=float(input('Введіть 1 катет рівнобедренного трикутника'))
        self.side2=float(input('Введіть 2 катет рівнобедренного трикутника'))

    def sq(self):
        self.square = 1 / 2*(self.side1 * self.side2)

    def P(self):
        self.perimeter=self.side1+self.side2+(math.square(self.side1**2+self.side2**2))

tr=rightTriangle()
tr.sq()