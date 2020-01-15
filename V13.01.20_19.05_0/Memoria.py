class Memoria:

    def __init__(self):
        self.__memoria = []

    def get_memoria(self):
        return self.__memoria

    def ordenar_memoria(self, populacao):
        for contador in range(len(populacao)):
            for contador2 in range(contador, len(populacao)):
                if populacao[contador].get_fitness() > populacao[contador2].get_fitness():
                    populacao[contador2], populacao[contador] = populacao[contador], populacao[contador2]

                    contador2 -= 1

        self.__memoria = populacao
