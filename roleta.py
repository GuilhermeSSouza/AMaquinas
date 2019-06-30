from random import *
from math import *



p = [1,2,5,4,7,6,6,8,8,10,8,7]

def roleta(p):

	pop_roleta = sorted(p, Key = min(p) reverse = True)
	print(pop_roleta)
	peso = [1,1,1,1,2,2,3,3,4,5,6,7]
	somaPeso = 0
	for i in range(len(peso)):
		somaPeso +=peso[i]

	print(somaPeso)
	sorteio = randint(0, somaPeso)
	print(sorteio)
	posicaoEscolhida = -1;
	while sorteio> 0:
		posicaoEscolhida+=1
		sorteio -=peso[posicaoEscolhida]

	return pop_roleta[posicaoEscolhida]


r = roleta(p)
print(r)