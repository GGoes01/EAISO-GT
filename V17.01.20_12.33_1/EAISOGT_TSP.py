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
        num_trocas = rnd.randint(1, int(len(rota_celula_mae)*.5))
        posicoes = [cont for cont in range(len(rota_celula_mae))]  # gera uma lista com valores de 0 até len(rota_mae)-1
        nova_rota = list(rota_celula_mae)  # copia a rota da celula mãe

        for cont in range(num_trocas):  # de acordo com o número de trocas
            pos_a = rnd.choice(posicoes)  # escolhe uma posição desntre as da lista
            posicoes.pop(posicoes.index(pos_a))  # remove a posição da lista

            pos_b = rnd.choice(posicoes)
            posicoes.pop(posicoes.index(pos_b))

            nova_rota[pos_a], nova_rota[pos_b] = nova_rota[pos_b], nova_rota[pos_a]

        return nova_rota

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

            # jogo = gt(populacao, num_rodadas=self.__num_rod, num_partidas=self.__num_par)
            # populacao = jogo.jogar()

            # for celula in populacao:
            #     print(celula.get__celula())
            #

            mem_temp = Memoria()
            mem_temp.ordenar_memoria(list(populacao))
            vetor_memoria_temp = mem_temp.get_memoria()

            for celula in vetor_memoria_temp:
                ja_existe = False

                for outra_celula in vetor_memoria:
                    if celula == outra_celula:
                        ja_existe = True

                if not ja_existe:
                    if celula.get_fitness() < vetor_memoria[-1].get_fitness():
                        vetor_memoria[-1] = celula
                        mem.ordenar_memoria(list(vetor_memoria))
                        vetor_memoria = mem.get_memoria()

            populacao = list(vetor_memoria)

            # for celula in populacao:
            #     print(celula.get__celula())

            num_eliminados = int(len(populacao)*0.6)

            for contador in range(num_eliminados):
                populacao.pop(-1)

            novas_celulas = Gerador(num_eliminados, cidades)
            pop_adicional = novas_celulas.gerar_populacao()

            populacao += pop_adicional

            print(ger, populacao[0].get_fitness(), populacao[0].get_rota())
