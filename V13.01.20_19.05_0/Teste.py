from Coordenada import Coordenada
from EAISOGT_TSP import EAISOGT_TSP

'''
Caminhos disponíveis:

paths/kroA100.tsp
paths/att532.tsp
paths/pcb1173.tsp
'''

eaisogt_tsp = EAISOGT_TSP(10, 1, 1, 1, "paths/kroA100.tsp")
eaisogt_tsp.executar()

