from math import ceil
class Quadrado():
    def __init__(self,comprimento,largura):
        self.comprimento = comprimento
        self.largura = largura
    def retornaComprimento(self):
        print("O valor do comprimento é de {}".format(self.comprimento))
    def retornaLargura(self):
        print("O valor da largura é de {}".format(self.largura))
    def calculaArea(self):
        return self.comprimento*self.largura
###Programa que utiliza a classe
c1 = int(input("Insira o comprimento do seu local em M: "))
l1 = int(input("Insira a largura do seu local em M: "))
print("-----===Carregando===-----\n\n\n")
ret1 = Quadrado(c1,l1)
print("A area do seu local é de {} M²".format(ret1.calculaArea()))