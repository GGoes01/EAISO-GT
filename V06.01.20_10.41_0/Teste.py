import random as rnd
from Celula import Celula
from Fitness import Fitness
from Populacao import Populacao
from GameTheory import GameTheory as gt
from Memoria import Memoria
from GeradorDeCelulas import Gerador


def mutacionar(fit_celula_mae):
    taxa_mutacao = fit_celula_mae * rnd.random() * rnd.choice([-1, 0, 1])
    fit_mutacionado = taxa_mutacao + fit_celula_mae
    return fit_mutacionado


def clonar(vetor_celulas, quantidade_de_clones):
    novo_vetor = []

    for celula in vetor_celulas:
        novo_vetor.append(celula)
        clones_bonus = int(quantidade_de_clones * celula.getAfinidade()/100)
        total_clones = clones_bonus + quantidade_de_clones

        for contador in range(total_clones):
            fit_mutacionado = mutacionar(celula.getFitness())
            celula_clone = Celula(celula.getValor(), fit_mutacionado, celula.getAfinidade(), 0, 0)
            novo_vetor.append(celula_clone)

            '''
            Instanciar uma nova célula, com as configurações da célula mãe para cada clone,
            além de apenas copiar
            '''
    return novo_vetor


def definir_afinidade(vetor):
    fit_total = 0
    maior_fitness = vetor[0].getFitness()

    for celula1 in vetor:
        fit_total += celula1.getFitness()
        if celula1.getFitness() > maior_fitness:
            maior_fitness = celula1.getFitness()

    fit_medio = fit_total/len(vetor)

    for celula1 in vetor:
        fitness = celula1.getFitness()
        afinidade = int(100*(fit_medio - fitness)/maior_fitness)
        celula1.setAfinidade(afinidade)

    return vetor


gerar = Gerador(30)
pop = Populacao()
pop.setPopulacao(gerar.gerarPopulacao())

vetor_celulas = pop.getPopulacao()

mem = Memoria()
vetor_memoria = vetor_celulas[:]
mem.ordenarMemoria(vetor_memoria)

vetor_celulas = definir_afinidade(vetor_celulas)

qtde_clones = 3

vetor_celulas = clonar(vetor_celulas[:], qtde_clones)

definir_afinidade(vetor_celulas[:])
jogo = gt(vetor_celulas[:], 10, 10)
vetor_celulas = jogo.jogar()


"""
Inserir método de ordenação com base no fitness
Eliminar os piores 60% da população
Comparar com vetor de memória
Ordenar vetor de memória
Repetir
"""

for celula in vetor_memoria:
    celula.imprimirCelula()

print()

for celula in vetor_celulas:
    celula.imprimirCelula()
print(len(vetor_celulas))
