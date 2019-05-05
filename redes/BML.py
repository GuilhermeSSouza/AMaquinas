#--------------------------------------------------------------------------------------------
#
# Backpropagation Multi Layer
#
# Machine Learning
# Prof: Marcelo Thielo
# Autor: Guilherme S. Santos    08/05/19
# 
#--------------------------------------------------------------------------------------------

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
def propagar_rede(rede, dados):
	entrada = dados
	for camada in rede:
		new_entrada = []
		for neuronio in camada:
			f_ativar = funcao_ativacao(neuronio['weights'], entrada)
			neuronio['saida'] = saida_neuro(f_ativar)
			new_entrada.append(neuronio['saida'])
		entrada = new_entrada
	return entrada




def transfer_derivative(saida):
	return saida * (1.0 - saida)

# Metodo que propaga o erra na rede- Erro é propado de tras pra frente na rede
def propagate_erro(rede, esperado_dados):
	for i in reversed(range(len(rede))):
		camada = rede[i]
		erro_list = list()
		if i != len(rede)-1:
			for j in range(len(camada)):
				error = 0.0
				for neuronioio in rede[i + 1]:
					error += (neuronioio['pesos'][j] * neuronioio['Delta'])
				erro_list.append(error)
		else:
			for j in range(len(camada)):
				neuronioio = camada[j]
				erro_list.append(esperado_dados[j] - neuronioio['saida'])
		for j in range(len(camada)):
			neuronioio = camada[j]
			neuronioio['Delta'] = erro_list[j] * transfer_derivative(neuronioio['saida'])


#Atualiza pesos antes de cada nova interação
def update_pesos(rede, dados, fator_att):
	for i in range(len(rede)):
		entrada = dados[:-1]
		if i != 0:
			entrada = [neuronioio['saida'] for neuronioio in rede[i - 1]]
		for neuronioio in rede[i]:
			for j in range(len(entrada)):
				neuronioio['pesos'][j] += fator_att * neuronioio['Delta'] * entrada[j]
			neuronioio['pesos'][-1] += fator_att * neuronioio['Delta']


#Treina a rede como dados segundo a quantidade
def treina_rede(rede, train, l_rate, n_epoch, n_saidas):
	for epoch in range(n_epoch):
		sum_error = 0
		for dados in train:
			saidas = propagate_erro(rede, dados)
			esperado = [0 for i in range(n_saidas)]
			esperado[dados[-1]] = 1
			sum_error += sum([(esperado[i]-saidas[i])**2 for i in range(len(esperado))])
			propagate_erro(rede, esperado)
			update_pesos(rede, dados, l_rate)
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))



rede = inicio_rede(3,5,2)
print(rede)
entrada = [1,1,0,None]
saida = []
saida = propagar_rede(rede, entrada)
print(saida)