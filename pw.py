from random import *
from math import *

K=2
Pop=[]
tamPop = 12


X = [[0,1], [1,2],[2,3],[4,1000], [5,1001],[6,4],[7,5], [8,6], [9,1002],[10, 1003], [11,1004], [12,1005]]

x = [1,2,3,1000,1001,4,5,6,1002,1003,1004, 1005]
N = len(x)

D = [[0.0 for i in range(N)] for j in range(N)]
D_1 = [[0.0 for i in range(N)] for j in range(N)]


#Distancia do valor Absoluto - Modulo
def distancia(a,b):
	return abs(a-b)


#Distancia Euclideana 
def dist_euclides(a,b):
	return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 )


#Função que ajusta media entre a dissimilaridade
def fator_media(v):
	p=0.0
	for i in range(0,N):
		p=p+float(M[i][v])
	if( p > 0 ):
		return p/float(N)
	else:
		return 1.0/float(N)


#Função de minimização da dissimilaridade entre os elementos
def min_function_dis(b):
	eps=0.0
	for r in range(0,K):
		acc = 0.0
		for i in range(0,N):
			for j in range(0,N):
				acc += b[i][r] * b[j][r] * D_1[i][j]
		eps+=acc/(2.0*fator_media(r)*N)
	return eps

for i in range (0,N):
	for j in range (0,N):
		D_1[i][j]=dist_euclides(X[i],X[j])

#print(D_1)


#Calula a Matriz de Dissimilaridade
for i in range (0,N):
	for j in range (0,N):
		D[i][j]=distancia(x[i],x[j])		


#Gera postenciais soluções
for j in range(0,tamPop):
	M = [[0 for i in range(K)] for y in range(N)]
	for i in range (0,N):
		M[i][randint(0,K-1)]=1

	Pop.append(M)
	


#Roleta, escolhe aleatoriamente baseado no ganho de minização, isto é os que são melhores soluções tem mais chance se ser escolhidos
def roleta(p):
	

	pop_roleta = sorted(p, key= min_function_dis, reverse = True)
	#print(pop_roleta)
	peso = [1,1,1,1,2,2,3,3,4,5,6,7]
	somaPeso = 0
	for i in range(len(peso)):
		somaPeso +=peso[i]

	#print(somaPeso)
	sorteio = randint(0, somaPeso)
	#print(sorteio)
	posicaoEscolhida = -1;
	while sorteio> 0:
		posicaoEscolhida+=1
		sorteio -=peso[posicaoEscolhida]

	return pop_roleta[posicaoEscolhida]


	#Defini  se ocorre ou não mutação
def mutacao(a):
	taxa_muta = randint(0,100)
	if taxa_muta < 20 :
		b = randint(0,N-1) 
		c = randint(0,K-1) 
		for i in range(0,K):
			a[b][i]=0
		a[b][c]=1
	return a


#Gerando nova familia de solução, filhos via seleção do mais apto
def crossover(a,b):
	c = a[:int(len(a)/2)]+b[int(len(b)/2):]
	d = b[:int(len(b)/2)]+a[int(len(a)/2):]
	return c,d


i = 0

bestSolve = 0
min_function_disMin = 100000
bestP = []
while i < 5000 :

	for q in range(len(Pop)):
		if min_function_dis(Pop[q]) < min_function_disMin:
			bestSolve = q
			min_function_disMin = min_function_dis(Pop[q])
			bestP.append(Pop[q])
		

	if(min_function_disMin < 30):
		break

	mP = Pop[bestSolve]
	pior = 0

	Pop2 = []
	for w in range(int(len(Pop)/2)):
		#Pai_1,Pai_2 = torneio(Pop)
		Pai_1 = roleta(Pop)
		Pai_2 = roleta(Pop)
		Filho_1,Filho_2 = crossover(Pai_1, Pai_2)
		Filho_1 = mutacao(Filho_1)
		Filho_2 = mutacao(Filho_2)
		
		if( min_function_dis(Filho_1) > pior ):
			pior = min_function_dis(Filho_1)
			f = 0
			LowSolve= 2*w+f
		if( min_function_dis(Filho_2) > pior ):	
			pior = min_function_dis(Filho_2)
			f = 1
			LowSolve= 2*w+f
		Pop2.append(Filho_1)
		Pop2.append(Filho_2)
	Pop = Pop2
	Pop[LowSolve] = mP
	i += 1


print('Lista de elementos para clusterização')
print (x)
print('   ')
print('Solução via Algoritimo genético')
print (bestP[-1])

