from math import ceil
class Retângulo():
    def __init__(self,comprimento,largura):
        self.comprimento = comprimento
        self.largura = largura
    def mudarValorComprimento(self,valor):
        self.comprimento = valor
    def mudarValorLargura(self,valor):
        self.largura = valor
    def retornaComprimento(self):
        print("O valor do comprimento é de {}".format(self.comprimento))
    def retornaLargura(self):
        print("O valor da largura é de {}".format(self.largura))
    def calculaArea(self):
        return self.comprimento*self.largura
    def calcularPerimetro(self):
        return  (self.comprimento*2) + (self.largura*2)
###Programa que utiliza a classe
c1 = int(input("Insira o comprimento do seu local em M: "))
l1 = int(input("Insira a largura do seu local em M: "))
print("-----===Carregando===-----\n\n\n")
ret1 = Retângulo(c1,l1)
print("A area do seu local é de {} M²".format(ret1.calculaArea()))
print("O perimetro do seu local é de {} \n\n\n".format(ret1.calcularPerimetro()))
print("-----===Pisos===-----\n\n\n")
piso = float(input("Insira a medida dos pisos em M² (use . ao invés de , ): "))
print("Você precisará de {} pisos para preencher o piso".format(ceil(ret1.calculaArea() / piso)))  # arredondamos o valor para cima, pois não podemos comprar 0.15 pisos, apenas valores inteiros
print("Você precisará de {} metros de rodapé".format(ret1.calcularPerimetro()))