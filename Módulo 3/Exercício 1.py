class Bola():
    def __init__(self,cor,circuferencia,material):
        self.cor=cor
        self.circuferencia=circuferencia
        self.material=material

    def trocacor(self,novaCor):
        self.cor=novaCor
        print("A cor da bola agora é {}".format(novaCor))


    def mostracor(self):
        corMostra = self.cor
        print("A cor da bola é {}".format(corMostra))


a = Bola("vermelha", 14, "plastico")
a.trocacor("roxo")
a.mostracor()