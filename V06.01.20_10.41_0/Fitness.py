import math


class Fitness:
    def __init__(self, Valores):
        self.valorA = Valores[0]
        self.valorB = Valores[1]

    def Schaffer(self):
        x2y2 = self.valorA**2 + self.valorB**2
        n = math.sin(math.sqrt(x2y2))**2 - 0.5
        d = (1 + 0.001*x2y2)**2
        fitness = 0.5 + (n/d)

        return fitness

    def DeJong(self):
        fitness = 100*(self.valorA**2 - self.valorB)**2 + (1 - self.valorA)**2

        return fitness
