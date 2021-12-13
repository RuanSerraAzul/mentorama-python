##Escreva um programa para resolver equações de 2º grau
##1: sem usar o módulo math
##2: usando o módulo math





###sem usar o metodo MAth
print('ax²+bx+c \n ax² = A  \n bx = b  \n c = c \n\n\n')
a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))
c = int(input("Insira o valor de C: "))
delta = b**2 - 4*a*c
raizDeDelta = delta**0.5
bhaskarapositivo = int((-b+ raizDeDelta)/2*a)
bhaskaranegativo = int((-b-raizDeDelta)/2*a)
print("X' = ",bhaskarapositivo,"\n")
print("X'' = ",bhaskaranegativo,"\n")

###Usando o método math
import math
print('ax²+bx+c \n ax² = A  \n bx = b  \n c = c \n\n\n')
a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))
c = int(input("Insira o valor de C: "))
delta = b**2 - 4*a*c
raizDeDelta = math.sqrt(delta)
bhaskarapositivo = int((-b+ raizDeDelta)/2*a)
bhaskaranegativo = int((-b-raizDeDelta)/2*a)
print("X' = ",bhaskarapositivo,"\n")
print("X'' = ",bhaskaranegativo,"\n")