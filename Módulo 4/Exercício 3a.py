####3 Remake do exercício 4 do módulo 1
### capturar um erro usando Try/Except:



#Escreva um programa que leia ois números e que pergunte qual operação você deseja realizar.
## Você deve poder:
## Calcular a soma, subtração, multiplicação e divisão

try:
    a = int(input("Insira o valor do primeiro numero:"))
except ValueError:
    print("Favor inserir um número válido")
    print("o valor do primeiro número por padrão em caso de erro será 1")
    a=1
else:
    print("Número computado")
finally:
    b = int(input("Insira o valor do segundo numero:"))
    c = str(input("Selecione a operação desejada: \n + para Soma \n - para subtração \n * para Multiplicação \n / para Divisão\n"))
    if c == "+":
        d = a+b
        print ("A soma dos dois números é igual a ", d)
    elif c == "-":
        d = a-b
        print ("A diferença dos dois números é igual a ", d)
    elif c == "*":
        d = a*b
        print ("A multiplicação entre os dois números é igual a ", d)
    elif c == "/":
        d = a/b
        print ("A divisão entre os dois números é igual a ", d)
    else:
        print("Favor inserir uma operação válida")
