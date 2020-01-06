class Celula:
    def __init__(self, Valor, Fitness, Afinidade, Comportamento, Ganho ):
        self.__valor = list(Valor)
        self.__fitness = Fitness
        self.__comportamento = Comportamento
        self.__ganho = Ganho
        self.__afinidade = Afinidade

    def getValor(self):
        return self.__valor

    def getFitness(self):
        return self.__fitness

    def getAfinidade(self):
        return self.__afinidade

    def getComportamento(self):
        return self.__comportamento

    def getGanho(self):
        return self.__ganho

    def setValor(self, Valor):
        self.__valor = list(Valor)

    def setFitness(self, Fitness):
        self.__fitness = Fitness

    def setAfinidade(self, Afinidade):
        self.__afinidade = Afinidade

    def setComportamento(self, Comportamento):
        self.__comportamento = Comportamento

    def setGanho(self, Ganho):
        self.__ganho = Ganho

    def imprimirCelula(self):
        print(f"Valores: {self.getValor()}, Fitness: {self.getFitness()}, Afinidade: {self.getAfinidade()} "
              f"Comportamento: {self.getComportamento()}, Ganho: {self.getGanho()}")
