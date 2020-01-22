import random
from Fitness import Fitness
from Celula import Celula


def calcular_afinidade(populacao):
    # fit_total = 0
    maior_fitness = populacao[0].get_fitness()

    for celula in populacao:
        # fit_total += celula.get_fitness()
        if celula.get_fitness() > maior_fitness:
            maior_fitness = celula.get_fitness()

    # fit_medio = fit_total/len(populacao)

    for celula in populacao:
        fitness = celula.get_fitness()
        afinidade = (maior_fitness - fitness)/maior_fitness
        celula.set_afinidade(afinidade)

    return populacao


class Gerador:

    def __init__(self, quantidade, cidades):
        self.__quantidade = quantidade
        self.__cidades = cidades

    def gerar_populacao(self):
        populacao = []

        for contador in range(self.__quantidade):
            rota = [pos for pos in range(len(self.__cidades))]  # rota = [0, 1, 2, 3, ..., 99]
            random.shuffle(rota)  # embaralha a rota
            fit = Fitness(rota, self.__cidades)  # calcula a distância total da rota definida
            fitiness = fit.calcular()  # define o fitness de acordo com a rota total
            celula = Celula(rota, fitiness, 0, 0, 0)  # instancia uma nova celula
            populacao.append(celula)  # adiciona a celula nova à população

        populacao = calcular_afinidade(populacao)

        return populacao

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade

    def get_quantidade(self):
        return self.__quantidade

    def set_cidades(self, cidades):
        self.__cidades = cidades

    def get_cidades(self):
        return self.__cidades
