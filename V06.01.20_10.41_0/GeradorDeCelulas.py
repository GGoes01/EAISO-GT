import random
from Celula import Celula
from Fitness import Fitness


class Gerador:
    def __init__(self, Quantidade):
        self.qtde = Quantidade

    def gerarPopulacao(self):

        vetorDeCelulas = []

        for cCelulas in range(self.qtde):

            valor = [random.randint(-100, 100), random.randint(-100, 100)]

            calculaFitness = Fitness(valor)
            fitness = calculaFitness.Schaffer()

            celula = Celula(valor, fitness, 0, 0, 0)

            vetorDeCelulas.append(celula)

        return vetorDeCelulas






