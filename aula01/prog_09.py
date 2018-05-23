def double(x):
	return x * 2

def my_message (message = "my default"):
	print message
	
def subtract (a = 0, b = 0):
	return a - b
	
print double(5)
my_message()
my_message("teste teste")
print subtract(4, 2)
print subtract(0, 5)
print subtract(b = 5)

stringtab = "data\tscience"
print stringtab
print len(stringtab)
