class Memoria():

    __memoria = []

    def getMemoria(self):
        return self.__memoria

    def ordenarMemoria(self, VetorCelulas):
        for contador in range(len(VetorCelulas)):
            for contador2 in range(contador, len(VetorCelulas)):
                if VetorCelulas[contador].getFitness() > VetorCelulas[contador2].getFitness():
                    aux = VetorCelulas[contador2]
                    VetorCelulas[contador2] = VetorCelulas[contador]
                    VetorCelulas[contador] = aux
                    contador2 -= 1

        self.__memoria = VetorCelulas
