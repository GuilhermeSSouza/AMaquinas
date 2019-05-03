import numpy as np
from random import random
from math import exp



#Cria a rede com 3 camadas, 1 - Entrada, 1 - Camada escondida 1- Saida
def inicio_rede(n_input, n_escondida, n_saida):
	rede = list()
	camada_escondida = [{'pesos':[random() for i in range(n_input+1)]} for i in range(n_escondida)]
	rede.append(camada_escondida)
	camada_saida = [{'pesos':[random() for i in range(n_escondida +1)]} for i in range(n_saida)]
	rede.append(camada_saida)
	return rede


def funcao_ativacao(peso_, entrada):
	valor =0
	m = len(peso_)
	for i in range(m-1):
		 valor += (peso_[i]*entrada[i])

	return valor + peso_[-1]



#função logistica ultilizada sobre o valor de ativação
def saida_neuro(valor):
	return 1.0/(1.0 + np.exp(-valor))



#Propagar dados pela rede
def propagar_rede(rede, entrada):
	entrada_propagada = entrada
	for camada in rede:
		entrada_nova = []
		for neuronio in camada:
			valor = funcao_ativacao(neuronio['pesos'], entrada_propagada)
			n_saida = saida_neuro(valor)
			entrada_nova.append(n_saida)
		entrada_propagada = entrada_nova
	return entrada_propagada









rede = inicio_rede(3,5,2)
print(rede)
entrada = [1,1,0,None]
saida = []
saida = propagar_rede(rede, entrada)
print(saida)