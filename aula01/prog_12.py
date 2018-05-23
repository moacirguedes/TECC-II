class Conjunto:

	def __init__(self, values=None):
		self.dict = {}
		if values is not None:
			for value in values:
				self.adicionar(value)
				
	def __repr__(self):
		return "Conjunto: " + str (self.dict.keys())
		
	def adicionar(self, value):
		self.dict[value] = True
	
	def contem(self, value):
		return value in self.dict
		
	def remove(self, value):
		del self.dict[value]
		

		
		
x = Conjunto([1, 2, 3, 2])
print x
x.adicionar(4)
print "contem 2? ", x.contem(2)
x.remove(3)
print x
print "contem 3? ",  x.contem(3)
