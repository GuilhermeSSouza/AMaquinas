from math import*
import numpy as np
from random import randint
from centroide import centroide, ponto



def readtable(name):
	f = open(name, 'r')
	lines = f.readlines()
	result = []
	for x in lines:
		result.append(x)
	f.close()
	tabela = []
	for x in range(0, len(result)):
		mydata = list(filter(None, (result[x].strip()).split(" ")))
		if (mydata):
			tabela.append(mydata)
	return tabela

data = readtable('data.dat')
data = np.matrix(data)
data = np.asanyarray(data)




class kmeans:
	def __init__(self):
		self.listc = []
		self.listpoint = []
		

	def geralabel(sel, data, k):

		for i in range(len(data)):
			n = randint(0, k)
			k = [n, data[i]]
			self.listpoint.append(k)
		return self.listpoint


	def retorna(self, data, label):
		dados = []
		for i in data:
			if i[1] == label:
				dados.append(i)

		return dados

	def addcentroide(self, dado, k):
		mx=0
		my=0
		n = len(dado)
		centro = []
		for i in dado:

			mx+= i[0]
			my+= i[1]

		dado = [k, [mx/n, my/n]]
		return dado


	def centro(self, dado, k):
		 listdados = geralabel(dado,k)
		 for i in range(k):
		 	 dadolabel = retorna(listdados, k)
		 	 centro = addcentroide(dadolabel, i)
		 	 self.listc.append(centro)


	def distancia(self, pontaA, pontoB):
		return = sqrt((pontoA[0]-pontoB[0])**2) + ((pontoA[1]-pontoB[1])**2)

	def calulacentroproximo(self, self.listc, self.listpoint, k):

		dist= []
		centros = self.listc

		for i in range(k):
			pontos = retorna(self.listpoint, i)

			for l in pontos:
				for  r in range(k)
				 dist.append(distancia(l, centros[r][1]))
				  i_label = dist.index(dist.min())
				 if i_label != i:
				 	



