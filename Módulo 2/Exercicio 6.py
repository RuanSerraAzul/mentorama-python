##Escreva uma função que receba uma string s como parametro e exiba a strign com espações suficientes a
##Frente para que a última letra da string esteja na coluna 70 da tela
def right_justify(s):
    while len(s)<70:
        s = ' '+ s
    return s
    
    
sim = "Whatsapp"
resultado = right_justify(sim)
print (resultado)