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
def inicio_rede(n_entrada, n_escondida, n_saida):
	rede = list()
	camada_escondida = [{'pesos':[random() for i in range(n_entrada+1)]} for i in range(n_escondida)]
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
	return 1.0/(1.0 + exp(-valor))



#Propagar dados pela rede
def propagar_rede(rede, dados):
	entrada = dados
	for camada in rede:
		new_entrada = []
		for neuronio in camada:
			f_ativar = funcao_ativacao(neuronio['pesos'], entrada)
			neuronio['saida'] = saida_neuro(f_ativar)
			new_entrada.append(neuronio['saida'])
		entrada = new_entrada
	return entrada




def funcao_derivada(saida):
	return saida * (1.0 - saida)

# Metodo que propaga o erra na rede- Erro é propado de tras pra frente na rede
def propaga_erro(rede, esperado_dados):
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
			neuronio['Delta'] = erro_list[j] * funcao_derivada(neuronio['saida'])


#Atualiza pesos antes de cada nova interação
#CORRIGIDO :   #Esse metodo ainda esta muito manual, para cada tamanho de saida deves se alterar o dados[- x:]. Onde x = tamnaho da saida
def update_pesos(rede, dados, fator_att):
	for i in range(len(rede)):
		entrada = dados
		if i != 0:
			entrada = [neuronio['saida'] for neuronio in rede[i - 1]]
		for neuronio in rede[i]:
			for j in range(len(entrada)):
				neuronio['pesos'][j] += fator_att * neuronio['Delta'] * entrada[j]
			neuronio['pesos'][-1] += fator_att * neuronio['Delta']


#Treina a rede como dados segundo a quantidade
def treina_rede(network, train, l_rate, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		sum_error = 0
		for row in train:
			saida = propagar_rede(network, row)
			esperndo = [0 for i in range(n_outputs)]
			esperndo = row[-n_outputs:]
			sum_error += sum([(esperndo[i]-saida[i])**2 for i in range(len(esperndo))])
			propaga_erro(network, esperndo)
			update_pesos(network, row[-n_outputs:], l_rate)
		print('>Epoch=%d, Erro=%.5f' % (epoch, sum_error))






#Metodo que propaga o dataset de verificação na rede após ela estar treinda
def test_rede(rede, row):
	outputs = propagar_rede(rede, row)
	return outputs



#CORRIGIDO: #SEM USO ATUAL: #Gambiara pra comverter uma  lista em uma string
def crianumero(row):
	saida = str(row[0]) +str(row[1]) + str(row[2]) + str(row[3])
	saida_t = str(row)
	return saida


#Dataset de treinamento números 1 e 2 em matrix de pixel
dataset_1=[[0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,0,1], [0,1,1,1,0,1,0,1,0,1,0,0,1,1,1,0,0,1,0]]


#Dataset de verificação com ruidos
dataset=[[0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,0,1], [0,1,1,0,0,1,0,1,0,1,0,0,1,1,1,0,0,1,0]]





#Carrega dados e cria a rede para treinamento
n_entrada = len(dataset_1[0]) - 4
n_saida = 4
network = inicio_rede(n_entrada, 2, n_saida)

#Parametros: (network, dataset, l_rate, epcoh, n_ouputs):  A REDE, o ARQUIVO DE DADOS, a taxa de aprendizado, numero de interações, numero de meuronios da camada de saida
treina_rede(network, dataset_1, 0.3, 10000, n_saida)



#Exibindo o resultado da rede

print('--------------------------- RESULTADO -------------------------------')
print( )
for row in dataset:
	saida  = str(row[-4:])
	prediction = test_rede(network, row)
	print('Esperado=%s, Obitido=%s' % (saida, prediction))