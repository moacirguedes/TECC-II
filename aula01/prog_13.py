x = range(10)
print "o tamanho de x eh ", len(x)
print "a soma dos elementos de x eh", sum(x)

print "o elemento na posicao 0 eh", x[0]
print "o elemento na posicao 1 eh", x[1]
x[1] = 10
print "o elemento na posicao 1 eh", x[1]
print "o ultimo elemento eh", x[-1]
print "o penultimo elemento eh", x[-2]

osTresPrimeirosDeX = x[:3]
print "tres primeiros elementos de x", osTresPrimeirosDeX
xSemExtremidades = x[1:-1]
print "elementos de x sem as estremidades", xSemExtremidades
osTresUltimosDeX = x[-3:]
print "tres ultimos elementos de x", osTresUltimosDeX



