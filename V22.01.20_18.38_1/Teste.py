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

eaisogt_tsp = EAISOGT_TSP(100, 10, 5, 5, "paths/kroA100.tsp")

inicio = time.time()
melhores, piores, media = eaisogt_tsp.executar()
fim = time.time()

print("Tempo total:", fim-inicio)

plt.figure(1)
plt.plot(melhores, 'blue', linewidth=0.8)
plt.plot(piores, 'red', linewidth=0.8)
plt.plot(media, 'black', linewidth=0.8)
plt.grid(True)
plt.xlabel('Geração')
plt.ylabel('Fitness')
plt.show()
