from cromossomo import Cromossomo
import random, time

class GABasico():

    def __init__(self, tamanho_populacao = 20, geracoes = 1000):

        self.populacao = []
        self.tam_populacao = tamanho_populacao
        self.geracoes = geracoes
        self.soma_avaliacoes = 0

    def inicializar_populacao(self):

        for i in range(self.tam_populacao):
            self.populacao.append(Cromossomo(100))
        for cromossomo in self.populacao: cromossomo.inicializar()

    def avaliar_populacao(self):

        self.soma_avaliacoes = 0
        for cromossomo in self.populacao:
            self.soma_avaliacoes += cromossomo.avaliar()

    def roleta(self):

        self.avaliar_populacao()
        limite = random.random() * self.soma_avaliacoes
        i, aux = [0, 0]
        random.shuffle(self.populacao)
        while aux < limite and i < self.tam_populacao:
            aux += self.populacao[i].avaliacao
            i += 1
        i -= 1
        return i

    def nova_geracao(self):

        nova_populacao = []
        for i in range(self.tam_populacao):
            pai1 = self.populacao[self.roleta()]
            pai2 = self.populacao[self.roleta()]
            filho = pai1.crossover(pai2)
            filho.mutacao(.05)
            nova_populacao.append(filho)
        return nova_populacao

    def executar(self):

        print("\n\nInicializando execucao do algorimo genético:...\n\n")
        self.inicializar_populacao()
        self.avaliar_populacao()
        ordenado = sorted(self.populacao, key = lambda x: x.avaliacao, reverse = True)
                   
            self.populacao = self.nova_geracao()
            self.avaliar_populacao()
            ordenado = sorted(self.populacao, key = lambda x: x.avaliacao, reverse = True)
        print('top 1 -> %s' % (ordenado[1]))
        
ga = GABasico(tamanho_populacao = 100, geracoes = 1000)
ga.executar()
