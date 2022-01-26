class bombaCombustivel():
    def __init__(self,tipoCombustivel,valorLitro,quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self,valor):
        litros = valor / self.valorLitro
        print("Abastecer {0} vai render {1} Litros".format(valor,litros))
        self.quantidadeCombustivel -= litros
        print("A quantidade de combustivel na bomba agora é {}".format(self.quantidadeCombustivel))

    def abastecerPorLitro(self,valor):
        custo = (self.valorLitro * valor)
        print("Abastecer {0} litros vai custar {1}R$".format(valor,custo))
        self.quantidadeCombustivel -= valor
        print("A quantidade de combustivel na bomba agora é {}".format(self.quantidadeCombustivel))

    def alterarValor(self,valor):
        self.valorLitro = valor
        print("O valor de gasolina pelo litro agora custa {}".format(self.valorLitro))

    def alterarCombustivel(self, combustivel):
        self.tipoCombustivel = combustivel
        print("O combustivel na bomba agora é {}".format("combustivel"))
        
    def alterarQuantitadeCombustivel(self,valor):
        self.quantidadeCombustivel = valor
        print("A quantidade de combstivel na bomba agora é {}".format(self.quantidadeCombustivel))


bomb = bombaCombustivel("Gasolina",6.12,500)
bomb.alterarCombustivel("Diesel")
bomb.abastecerPorLitro(10)
bomb.abastecerPorValor(61.20)
bomb.alterarQuantitadeCombustivel(500)