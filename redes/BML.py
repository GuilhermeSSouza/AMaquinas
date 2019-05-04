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
		for neuronioio in camada:
			valor = funcao_ativacao(neuronioio['pesos'], entrada_propagada)
			n_saida = saida_neuro(valor)
			entrada_nova.append(n_saida)
		entrada_propagada = entrada_nova
	return entrada_propagada




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
				for neuronio in rede[i + 1]:
					error += (neuronio['pesos'][j] * neuronio['Delta'])
				erro_list.append(error)
		else:
			for j in range(len(camada)):
				neuronio = camada[j]
				erro_list.append(esperado_dados[j] - neuronio['saida'])
		for j in range(len(camada)):
			neuronio = camada[j]
			neuronio['Delta'] = erro_list[j] * transfer_derivative(neuronio['saida'])


#Atualiza pesos
def update_pesos(rede, dados, fator_att):
	for i in range(len(rede)):
		entrada = dados[:-1]
		if i != 0:
			entrada = [neuronio['saida'] for neuronio in rede[i - 1]]
		for neuronio in rede[i]:
			for j in range(len(entrada)):
				neuronio['pesos'][j] += fator_att * neuronio['Delta'] * entrada[j]
			neuronio['pesos'][-1] += fator_att * neuronio['Delta']



def treina_rede(rede, train, l_rate, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		sum_error = 0
		for row in train:
			outputs = forward_propagate(rede, row)
			esperado = [0 for i in range(n_outputs)]
			esperado[row[-1]] = 1
			sum_error += sum([(esperado[i]-outputs[i])**2 for i in range(len(esperado))])
			propagate_erro(rede, esperado)
			update_pesos(rede, row, l_rate)
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))



rede = inicio_rede(3,5,2)
print(rede)
entrada = [1,1,0,None]
saida = []
saida = propagar_rede(rede, entrada)
print(saida)