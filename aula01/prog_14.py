def soma_e_produto(x, y):
	return (x+y), (x*y)
	
sp = soma_e_produto(3,5)
print sp
#sp[1] = 45
s, p = soma_e_produto(2, 3)
print s
print p
p = 45
print p

x, y = 1, 2
x, y = y, x
print x, y

nota = {"Joel": 8.5, "Tim": 4.5}
print "a Nota de Joel foi", nota["Joel"]
print "a nota de Joel foi", nota.get("Joel", 0)

try:
	print "Julia tem nota?", nota["Julia"]
except KeyError:
	print "Julia nao tem nota"

