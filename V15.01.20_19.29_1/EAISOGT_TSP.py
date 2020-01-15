from Coordenada import Coordenada
from Gerador import Gerador
from Gerador import calcular_afinidade
from Celula import Celula
from Memoria import Memoria
from Fitness import Fitness
from GameTheory import GameTheory as gt
import random as rnd

class EAISOGT_TSP:

    def __init__(self, num_cel, num_ger, num_par, num_rod, file):
        self.__num_cel = num_cel
        self.__num_ger = num_ger
        self.__num_par = num_par
        self.__num_rod = num_rod
        self.__file = file

    def mutacionar(self, rota_celula_mae):
        num_trocas = rnd.randint(1, len(rota_celula_mae)*.5)
        rota_nova = list(rota_celula_mae)

        for cont in range(num_trocas):
            pos_a = rnd.randint(0, len(rota_celula_mae) - 1)
            pos_b = rnd.randint(0, len(rota_celula_mae) - 1)

            while pos_a == pos_b:
                pos_a = rnd.randint(0, len(rota_celula_mae) - 1)
                pos_b = rnd.randint(0, len(rota_celula_mae) - 1)

            rota_nova[pos_a], rota_nova[pos_b] = rota_nova[pos_b], rota_nova[pos_a]

        return rota_nova

    def clonar(self, vetor_celulas, quantidade_de_clones, cidades):
        novo_vetor = []

        for celula in vetor_celulas:
            novo_vetor.append(celula)
            clones_bonus = int(quantidade_de_clones * celula.get_afinidade())
            total_clones = clones_bonus + quantidade_de_clones

            for contador in range(total_clones):
                rota_mutacionada = self.mutacionar(list(celula.get_rota()))
                fit = Fitness(rota_mutacionada, cidades)
                fitness = fit.calcular()
                celula_clone = Celula(rota_mutacionada, fitness, 0, 0, 0)
                novo_vetor.append(celula_clone)

        return novo_vetor

    def executar(self):
        coord = Coordenada(self.__file)
        cidades = coord.ler_coordenadas()

        pop = Gerador(self.__num_cel, cidades)
        populacao = pop.gerar_populacao()

        mem = Memoria()
        vetor_memoria = list(populacao)
        mem.ordenar_memoria(vetor_memoria)
        for ger in range(self.__num_ger):

            num_clones = int(self.__num_cel*0.1)

            populacao = self.clonar(populacao, num_clones, cidades)
            populacao = calcular_afinidade(populacao)

            jogo = gt(populacao, num_rodadas=self.__num_rod, num_partidas=self.__num_par)
            populacao = jogo.jogar()

            for celula in populacao:
                print(celula.get__celula())

