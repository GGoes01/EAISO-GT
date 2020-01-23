import time
import matplotlib.pyplot as plt
from EAISOGT_TSP import EAISOGT_TSP

'''
Caminhos disponíveis:

paths/bayg29.tsp
paths/kroA100.tsp
paths/att532.tsp
paths/pcb1173.tsp
'''

melhores = []
piores = []
medias = []

num_eras = 5
pop_ini = 100
num_geracoes = 1000
num_rodadas = 5
num_partidas = 5
evolucao = True
game_theory = True
mapa = "paths/kroA100.tsp"

nome_arq = mapa.replace('.tsp', '_') + str(num_eras) + '_' + str(pop_ini) + evolucao * "_E"\
           + game_theory * "_GT" + '.ggflog'
arq = open(nome_arq, "w", encoding='utf-8')

arq.write("MAPA: " + str(mapa) + "\n")
arq.write("QTDE. ERAS: " + str(num_eras) + "\n")
arq.write("POP. INICIAL: " + str(pop_ini) + "\n")
arq.write("QTDE. GERAÇÕES: " + str(num_geracoes) + "\n")
arq.write("QTDE. PARTIDAS: " + str(num_partidas) + "\n")
arq.write("QTDE. RODADAS: " + str(num_rodadas) + "\n")
arq.write("EVOLUÇÃO: " + str(evolucao) + "\n")
arq.write("GAME THEORY: " + str(game_theory) + "\n\n")

eaisogt_tsp = EAISOGT_TSP(pop_ini, num_geracoes,  num_partidas, num_rodadas, mapa, evolutionary=evolucao,
                          game_theory=game_theory)
for era in range(num_eras):
    arq.write("ERA: " + str(era + 1) + "\n")
    print(era)

    inicio = time.time()
    melhores_aux, piores_aux, medias_aux = eaisogt_tsp.executar()
    fim = time.time()

    melhores += melhores_aux
    piores += piores_aux
    medias += medias_aux

    tempo = fim - inicio

    arq.write(str(melhores_aux) + "\n")
    arq.write(str(piores_aux) + "\n")
    arq.write(str(medias_aux) + "\n")
    arq.write("TEMPO EXECUÇÃO: " + str(tempo) + "\n\n")

nome_graf = nome_arq.replace(".ggflog", ".png")
nome_graf = nome_graf.replace("paths/", "")

arq.close()

plt.figure(1)
plt.plot(melhores, 'blue', linewidth=0.8)
plt.plot(piores, 'red', linewidth=0.8)
plt.plot(medias, 'black', linewidth=0.8)
plt.grid(True)
plt.xlabel('Geração')
plt.ylabel('Fitness')
plt.axis([0, len(melhores), 0, 210000])
plt.savefig("graphs/" + nome_graf)
