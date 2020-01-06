from Celula import Celula
import random


def aplicarPenalidade(fitness, ganho, rodadas, partidas):
    temptation = 24

    penalidade = fitness * 10 ** -((temptation * rodadas * partidas) / ganho)
    penalidade += fitness

    return penalidade


def ordenarVetorFitness(vetorCelulas):
    for cont in range(len(vetorCelulas)):
        for cont2 in range(cont, len(vetorCelulas)):
            if vetorCelulas[cont].getFitness() > vetorCelulas[cont2].getFitness():
                aux = vetorCelulas[cont2]
                vetorCelulas[cont2] = vetorCelulas[cont]
                vetorCelulas[cont] = aux
                cont2 -= 1
    return vetorCelulas


def ordenarVetorDilema(vetorCelulas):
    for cont in range(len(vetorCelulas)):
        for cont2 in range(cont, len(vetorCelulas)):
            if vetorCelulas[cont].getGanho() > vetorCelulas[cont2].getGanho():
                aux = vetorCelulas[cont2]
                vetorCelulas[cont2] = vetorCelulas[cont]
                vetorCelulas[cont] = aux
                cont2 -= 1

    return vetorCelulas


class GameTheory:

    def __init__(self, Celulas, NumeroDePartidas, NumeroDeRodadas):
        self.dilema = list(Celulas)
        self.numeroDePartidas = NumeroDePartidas
        self.numeroDeRodadas = NumeroDeRodadas

    def jogar(self):

        vAdversarios = []
        vCelulasOrdena = []
        vRetorna = []
        vTemp = []

        reward = 18
        punishment = 6
        temptation = 24
        sucker = 3

        tamanho = int(len(self.dilema)/2)

        '''
        Cria o vetor de adversarios
        '''

        for cAdversarios in range(tamanho):
            vAdversarios.append([0, 0])

        for cCelulas in range(tamanho*2):
            vCelulasOrdena.append(0)
            vRetorna.append(0)

        if self.numeroDePartidas != 0:
            for b in range(tamanho):
                for a in range(2):
                    limite = len(self.dilema) - 1
                    valor = random.randint(0, limite)
                    celula = self.dilema[valor]
                    self.dilema.pop(valor)
                    comportamento = random.randint(0, 2)
                    celula.setComportamento(comportamento)
                    celula.setGanho(0)
                    vAdversarios[b][a] = celula
                    # vAdversarios[b][a].imprimirCelula()

            '''
            Ordena as células de acordo com o fitness, caso o numero de partidas seja igual a 0
            '''
        else:
            for a in range(len(vCelulasOrdena)):
                vCelulasOrdena[a] = self.dilema[0]
                self.dilema.pop(0)

            vCelulasOrdena = ordenarVetorFitness(vCelulasOrdena)

            vI = int(len(vCelulasOrdena)/2)
            vF = len(vCelulasOrdena)

            for a in range(vI, vF):
                vCelulasOrdena.pop(vI)

            vRetorna = vCelulasOrdena

        '''
        Inicia a disputa
        '''
        for cPartidas in range(self.numeroDePartidas):
            for cRodadas in range(self.numeroDeRodadas):
                for cAdversarios in range(len(vAdversarios)):

                    comportamentoAleatorio1 = False
                    comportamentoAleatorio2 = False
                    '''
                    Atribui um valor aleatório para as células
                    '''
                    if vAdversarios[cAdversarios][0].getComportamento() == 2:
                        comportamentoAleatorio1 = True
                        valor = random.randint(0, 1)
                        vAdversarios[cAdversarios][0].setComportamento(valor)

                    if vAdversarios[cAdversarios][1].getComportamento() == 2:
                        comportamentoAleatorio2 = True
                        valor = random.randint(0, 1)
                        vAdversarios[cAdversarios][1].setComportamento(valor)

                    comportamentoA = vAdversarios[cAdversarios][0].getComportamento()
                    comportamentoB = vAdversarios[cAdversarios][1].getComportamento()


                    '''
                    Caso as duas possuam comportamento iguais
                    '''
                    if comportamentoA == comportamentoB:
                        '''
                        Caso as duas cooperem
                        '''
                        if comportamentoA == 0:
                            ganhoA = vAdversarios[cAdversarios][0].getGanho()
                            ganhoB = vAdversarios[cAdversarios][1].getGanho()

                            vAdversarios[cAdversarios][0].setGanho(ganhoA + reward)
                            vAdversarios[cAdversarios][1].setGanho(ganhoB + reward)

                        '''
                        Caso as duas traiam
                        '''
                        if comportamentoA == 1:
                            ganhoA = vAdversarios[cAdversarios][0].getGanho()
                            ganhoB = vAdversarios[cAdversarios][1].getGanho()

                            vAdversarios[cAdversarios][0].setGanho(ganhoA + punishment)
                            vAdversarios[cAdversarios][1].setGanho(ganhoB + punishment)

                    else:
                        '''
                        Caso os comportamentos sejam diferentes, uma coopere e a outra traia
                        '''
                        if comportamentoA == 0:
                            ganhoA = vAdversarios[cAdversarios][0].getGanho()
                            ganhoB = vAdversarios[cAdversarios][1].getGanho()

                            vAdversarios[cAdversarios][0].setGanho(ganhoA + sucker)
                            vAdversarios[cAdversarios][1].setGanho(ganhoB + temptation)

                        if comportamentoA == 1:
                            ganhoA = vAdversarios[cAdversarios][0].getGanho()
                            ganhoB = vAdversarios[cAdversarios][1].getGanho()

                            vAdversarios[cAdversarios][0].setGanho(ganhoA + temptation)
                            vAdversarios[cAdversarios][1].setGanho(ganhoB + sucker)

                    if comportamentoAleatorio1:
                        vAdversarios[cAdversarios][0].setComportamento(2)

                    if comportamentoAleatorio2:
                        vAdversarios[cAdversarios][1].setComportamento(2)

                #    vAdversarios[cAdversarios][0].imprimirCelula()
                #    vAdversarios[cAdversarios][1].imprimirCelula()

                    vTemp.append(vAdversarios[cAdversarios][0])
                    vTemp.append(vAdversarios[cAdversarios][1])

                random.shuffle(vTemp)
                #print("")
                '''
                Muda a configuração de adversários,
                para que haja variação de confrontos
                no final de cada rodada
                '''
                for c1 in range(tamanho):
                    for c2 in range(2):
                        limite = len(vTemp) - 1
                        valor = random.randint(0, limite)
                        celula = vTemp[valor]
                        vTemp.pop(valor)
                        vAdversarios[c1][c2] = celula

            vTemp = []
            for cAdversarios in range(len(vAdversarios)):
                vTemp.append(vAdversarios[cAdversarios][0])
                vTemp.append(vAdversarios[cAdversarios][1])

            cCelulas = 0
            vCelulas = []
        #    print(len(vCelulas))
            while len(vTemp) > 0:
                valor = len(vTemp)
                celula = vTemp[valor - 1]
                vTemp.pop(valor - 1)
                vCelulas.append(celula)
            #    vCelulas[cCelulas].imprimirCelula()
                cCelulas += 1

            '''
            for celula in range(len(vCelulas)):
                vCelulas[celula].imprimirCelula()
            #'''

            vCelulas = ordenarVetorDilema(vCelulas)

            '''
            for celula in range(len(vCelulas)):
                vCelulas[celula].imprimirCelula()
            '''

            # vI = int(len(vCelulas) * 0.5)
            # vF = len(vCelulas)
            #
            # for cCelulas in range(vI, vF):
            #     vCelulas.pop(vI)

            # print("")

            '''
            for celula in range(len(vCelulas)):
                vCelulas[celula].imprimirCelula()
            '''

            vRetorna = vCelulas

        for celula in vRetorna:
            taxa_penalidade = celula.getGanho()/(temptation*self.numeroDePartidas*self.numeroDeRodadas)
            penalidade = (1 + taxa_penalidade) * celula.getAfinidade()
            celula.setAfinidade(int(penalidade))

        return vRetorna
