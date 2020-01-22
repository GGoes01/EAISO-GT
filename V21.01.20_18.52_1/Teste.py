import time
from EAISOGT_TSP import EAISOGT_TSP

'''
Caminhos disponíveis:

paths/bayg29.tsp
paths/kroA100.tsp
paths/att532.tsp
paths/pcb1173.tsp
'''

eaisogt_tsp = EAISOGT_TSP(100, 100, 5, 5, "paths/kroA100.tsp")

inicio = time.time()
eaisogt_tsp.executar()
fim = time.time()

print("Tempo total:", fim-inicio)
