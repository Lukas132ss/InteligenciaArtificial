import numpy as np


class Vertice:

    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacente = []

    def adiciona_adjacente(self, adjacente):
        self.adjacente.append(adjacente)

    def mostra_adjacente(self):
        for i in self.adjacente:
            print(i.vertice.rotulo, i.custo)


class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo


class Grafo:
    pf = Vertice('Paulo Frontin', 172)
    pu = Vertice('Porto União', 203)
    canoinhas = Vertice('Canoinhas', 141)
    tresb = Vertice('Três Barras', 131)
    sm = Vertice('São Matheus', 123)
    irati = Vertice('Irati', 139)
    cwb = Vertice('Curitiba', 0)
    palmeira = Vertice('Palmeira', 59)
    mafra = Vertice('Mafra', 94)
    cl = Vertice('Campo Largo', 27)
    bn = Vertice('Balsa Nova', 41)
    lapa = Vertice('Lapa', 74)
    ts = Vertice('Tijucas do Sul', 56)
    araucaria = Vertice('Araucária', 23)
    sjp = Vertice('São José dos Pinhais', 13)
    contenda = Vertice('Contenda', 39)

    pf.adiciona_adjacente(Adjacente(irati, 75))
    pf.adiciona_adjacente(Adjacente(pu, 46))

    pu.adiciona_adjacente(Adjacente(canoinhas, 78))
    pu.adiciona_adjacente(Adjacente(pf, 46))
    pu.adiciona_adjacente(Adjacente(sm, 87))

    canoinhas.adiciona_adjacente(Adjacente(pu, 78))
    canoinhas.adiciona_adjacente(Adjacente(mafra, 66))
    canoinhas.adiciona_adjacente(Adjacente(tresb, 12))

    tresb.adiciona_adjacente(Adjacente(canoinhas, 12))
    tresb.adiciona_adjacente(Adjacente(sm, 43))

    sm.adiciona_adjacente(Adjacente(pu, 87))
    sm.adiciona_adjacente(Adjacente(irati, 57))
    sm.adiciona_adjacente(Adjacente(tresb, 43))
    sm.adiciona_adjacente(Adjacente(palmeira, 77))
    sm.adiciona_adjacente(Adjacente(lapa, 60))

    irati.adiciona_adjacente(Adjacente(pf, 75))
    irati.adiciona_adjacente(Adjacente(palmeira, 75))
    irati.adiciona_adjacente(Adjacente(sm, 57))

    palmeira.adiciona_adjacente(Adjacente(irati, 75))
    palmeira.adiciona_adjacente(Adjacente(sm, 77))
    palmeira.adiciona_adjacente(Adjacente(cl, 55))

    mafra.adiciona_adjacente(Adjacente(lapa, 57))
    mafra.adiciona_adjacente(Adjacente(canoinhas, 66))
    mafra.adiciona_adjacente(Adjacente(ts, 99))

    cl.adiciona_adjacente(Adjacente(palmeira, 55))
    cl.adiciona_adjacente(Adjacente(cwb, 29))
    cl.adiciona_adjacente(Adjacente(bn, 22))

    bn.adiciona_adjacente(Adjacente(cl, 22))
    bn.adiciona_adjacente(Adjacente(cwb, 51))
    bn.adiciona_adjacente(Adjacente(contenda, 18))

    lapa.adiciona_adjacente(Adjacente(mafra, 57))
    lapa.adiciona_adjacente(Adjacente(contenda, 26))
    lapa.adiciona_adjacente(Adjacente(sm, 60))

    ts.adiciona_adjacente(Adjacente(sjp, 49))
    ts.adiciona_adjacente(Adjacente(mafra, 99))

    araucaria.adiciona_adjacente(Adjacente(cwb, 37))
    araucaria.adiciona_adjacente(Adjacente(contenda, 18))

    sjp.adiciona_adjacente(Adjacente(ts, 49))
    sjp.adiciona_adjacente(Adjacente(cwb, 15))

    contenda.adiciona_adjacente(Adjacente(lapa, 26))
    contenda.adiciona_adjacente(Adjacente(bn, 19))
    contenda.adiciona_adjacente(Adjacente(araucaria, 18))

    cwb.adiciona_adjacente(Adjacente(sjp, 15))
    cwb.adiciona_adjacente(Adjacente(araucaria, 37))
    cwb.adiciona_adjacente(Adjacente(bn, 51))
    cwb.adiciona_adjacente(Adjacente(cl, 29))


grafo = Grafo()


class vetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=object)

    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capaxidade máxima atingida.')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print('o vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].vertice.rotulo, ' - ',
                      self.valores[i].custo, ' - ',
                      self.valores[i].vertice.distancia_objetivo, ' - ',
                      self.valores[i].distancia_aestrela)


class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('------------------')
        print('Atual: {}'.format(atual.rotulo))
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = vetorOrdenado(len(atual.adjacente))
            for adjacente in atual.adjacente:
                if adjacente.vertice.visitado == False:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0].vertice)


busca_aestrela = AEstrela(grafo.cwb)
busca_aestrela.buscar(grafo.pu)
