class ponto:
	"""docstring for centroide"""
	def __init__(self, label):
		self.label = label
		self.pontos = []
		self.centro = None


	def getlabel(self):
		return self.label

	def getpoint(self):
		return self.pontos

	def addpoint(self, pontos):
		self.pontos.append(pontos)

	def removepont(self,ponto_remove):
		self.pontos.remove(ponto_remove)

	def getcentroide(self):
		return self.centro

	def addcentroide(self, centroide):
		self.centro = centroide
		


class centroide:

	def __init__(self,label):
		self.label = label
		self.position = None

	def getlabel(self):
		return self.label

	def getpoint(self):
		return self.position

	def addposition(self, position):
		self.position = position


