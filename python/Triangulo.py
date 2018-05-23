class Triangulo:
    def __init__(self, values=None):
        self.dict = {}
        if values is not None:
            for value in values:
                self.adicionar(value)

    def __repr__(self):
        return "triangulo: " + str(self.dict.keys())

    def adicionar(self, value):
        self.dict[value] = True

    def ehTriangulo(self):
        a = list(self.dict)[0]
        b = list(self.dict)[1]
        c = list(self.dict)[2]

        if ((a + b + c) == 180):
            return True
        else:
            return False

    def tipo(self):
        return "equilatero"


x = Triangulo([40, 60, 81])
print x
print x.ehTriangulo()
print x

"""
Criar classe triangulo baseado na classe conjunto q o prof passou 

1) Classificar o triangulo em retangulo, obtusangulo ou acutangulo
(ele é valido se e somente se a soma dos angulos for 180) 
"""