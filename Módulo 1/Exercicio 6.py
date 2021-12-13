## Escreva um programa para contar quantos numeros pares e impares existentes de 1 até 10.  bem como a soma deles
## 1: usando o while.
##  2: usando o for, range e sum

####Usando while
c = 1
pares = 0
impares = 0
somapares = 0
somaimpares = 1
while c<=10:
    if c%2 != 1:
        pares+=1
        somapares+=c
    else:
        impares+=1
        somaimpares+=c
    c+=1
print("De 1 a 10 existem ",pares," números pares e ",impares, "números impares")
print("Soma dos pares =",somapares, "soma dos impares=",somaimpares)

###Usando Range e sum
c = 1
pares = 0
impares = 0
somapares = 0
somaimpares = 1
for c in range(11):
    if c%2 != 1:
        pares+=1
        somapares+=c
    else:
        impares+=1
        somaimpares+=c
    c+=1
print("De 1 a 10 existem ",pares," números pares e ",impares, "números impares")
print("Soma dos pares =",somapares, "soma dos impares=",somaimpares)
