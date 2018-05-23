""" 
aqui tem um 
comentario de varias linhas 
"""
def ehPar (num):
	if (num % 2 == 0):
		return True
	else:
		return False

		
for i in range(5):
	print ehPar(i)
	
i = 10
while i < 15:
	print ehPar(i)
	i+=  1
	
	
	