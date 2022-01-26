class Carro():
    def __init__(self,modelo,cor,combustivel,marca):
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        self.marca = marca

    def exibeCarro(self):
        print("O modelo do carro é {0}, ele é da cor {1},roda usando {2}, e é da marca {3}".format(self.modelo,self.cor,self.combustivel,self.marca))

    def mudaCor(self,cor):
        self.cor = cor
        print("O carro {0} agora é da cor {1}".format(self.modelo,cor))

    def mudarCombustivel(self,combustivel):
        self.combustivel = combustivel
        print("O carro {0} passou por reformas e agora roda usando {1}".format(self.modelo,combustivel))

hb20 = Carro("HB20","Branco","Diesel","Hyundai")
hb20.exibeCarro()

corolla = Carro("Corolla","Preto","Gasolina","Toyota")
corolla.mudaCor("Vermelho")

celta = Carro("Celta","Prata","Gás","Chevrolet")
celta.mudarCombustivel("Gasolina")
        