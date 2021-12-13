##Escreva um programa que reca como entrada do usuario o nome "João" sobrenome "da Silva", idade "25",
## Cidade "São Paulo", ddd "11", Telefone "3333-3333" e faça as seguintes instruções:
##imprima na tela o nome completo em uma unica linha
##imprima na tea o telfone com o DDD em uma unica linha
## imprima na tela a idade
## imprima na tela a cidade

nome = input('qual é seu nome? ')
sobrenome = input('qual é seu sobrenome? ')
idade = int(input('qual é sua idade? '))
cidade = input('qual a sua cidade? ')
ddd = int(input('qual é seu DDD '))
telefone = int(input('qual é seu telefone? \n'))

print(nome,sobrenome ,'\n')
print('(',ddd,')',telefone ,'\n')
print(idade ,'\n')
print(cidade)