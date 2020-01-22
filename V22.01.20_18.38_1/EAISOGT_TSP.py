from Coordenada import Coordenada
from Gerador import Gerador
from Gerador import calcular_afinidade
from Celula import Celula
from Memoria import Memoria
from Memoria import recuperar_memoria
from Fitness import Fitness
from GameTheory import GameTheory as gt
import random as rnd
import os


class EAISOGT_TSP:

    def __init__(self, num_cel, num_ger, num_par, num_rod, file):
        self.__num_cel = num_cel
        self.__num_ger = num_ger
        self.__num_par = num_par
        self.__num_rod = num_rod
        self.__file = file
        self.__arquivo_memoria = file + str(num_cel) + '.ggf'

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

        melhores_fitness = []  # lista preenchida com o melhor fitness de cada geração
        piores_fitness = []  # lista preenchida com os piores fitness de cada geração
        medias = []  # lista preenchida com a media dos fitness de cada geração

        if os.path.isfile(self.__arquivo_memoria):
            rotas = recuperar_memoria(self.__arquivo_memoria)

            for celula in populacao:
                celula.set_rota(list(rotas[0]))
                rotas.pop(0)
                fit = Fitness(celula.get_rota(), cidades)
                fitness = fit.calcular()
                celula.set_fitness(fitness)

            populacao = calcular_afinidade(populacao)

        mem = Memoria()
        vetor_memoria = list(populacao)
        mem.ordenar_memoria(vetor_memoria)
        for ger in range(self.__num_ger):

            num_clones = int(self.__num_cel*0.1)

            populacao = self.clonar(populacao, num_clones, cidades)
            populacao = calcular_afinidade(populacao)

            jogo = gt(populacao, num_rodadas=self.__num_rod, num_partidas=self.__num_par)
            populacao = jogo.jogar()

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

            mem.registrar_memoria(self.__arquivo_memoria)

            melhor_fitness = populacao[0].get_fitness()
            pior_fitness = populacao[0].get_fitness()
            fit_total = 0

            for celula in populacao:
                if celula.get_fitness() < melhor_fitness:
                    melhor_fitness = celula.get_fitness()

                elif celula.get_fitness() > pior_fitness:
                    pior_fitness = celula.get_fitness()

                fit_total += celula.get_fitness()

            media = fit_total/len(populacao)

            populacao = list(vetor_memoria)

            num_eliminados = int(len(populacao)*0.95)

            for contador in range(num_eliminados):
                populacao.pop(-1)

            novas_celulas = Gerador(num_eliminados, cidades)
            pop_adicional = novas_celulas.gerar_populacao()

            populacao += pop_adicional

            print(ger, populacao[0].get_fitness(), populacao[0].get_rota())

            melhores_fitness.append(melhor_fitness)
            piores_fitness.append(pior_fitness)
            medias.append(media)

        return melhores_fitness, piores_fitness, medias
