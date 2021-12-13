#3Escreva um programa que leia ois números e que pergunte qual operação você deseja realizar. Você deve poder
## Calcular a soma, subtração, multiplicação e divisão

a = int(input("Insira o valor do primeiro numero "))
b = int(input("Insira o valor do segundo numero "))
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

