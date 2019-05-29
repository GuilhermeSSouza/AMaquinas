import random
import math


dado = [[-1,1,1],[-1,-1,-1],[1,1,1]]



def distancia(valor, dado):
	a = 0
	for i in range(len(dado)):
		a +=(valor[i] - dado[i])**2
	return math.sqrt(a)


def knn(test, dado):
	v = []
	for i in range(len(dado)):
		t = [distancia(test,dado[:-1]),dado[-1]]
		v.append(t)

	return v
	
def k(k, v):
	a = 0
	b = 0
	vetor = v.sort()
	for i in range(len(vetor)):
		if vetor[1][i] == 1:
			a +=1
		else:
			b +=1

	if a>b:
		return 1

	else:
		return -1


test = [-0.987, 1.002]

r = knn(test, dado)

j = k(2, r)

print(j)