f= open('Módulo 4/Entrada exercício 1.txt','r')
lista= f.readlines()
f.close()
listaipvalidos= ""
listaipinvalidos = ""
for i in range (len(lista)):

    lista2 = lista[i].rsplit(".")

    if (int(lista2[0])<=255 and int(lista2[1])<=255 and int(lista2[2])<=255 and int(lista2[3])<=255):        listaipvalidos+=lista[i] + "\n"
    else:
        listaipinvalidos+=lista[i] + "\n"

saida = open('Módulo 4/Saída Exercício 1.txt','w+')
saida.write("[IP Validos]\n")
ipval="".join(listaipvalidos)
saida.write(ipval)
saida.write("\n\n\n")
saida.write("[IP Invalidos]\n")
ipinval = "".join(listaipinvalidos)
saida.write(ipinval)