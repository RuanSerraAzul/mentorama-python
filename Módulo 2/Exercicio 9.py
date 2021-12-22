caract=[]
nums=[]
ordem = ["0","1","2","3","4","5","6","7","8","9"]

gtLst=input("Digite sua sequência")

for e in gtLst:
    if e in ordem:
        nums.append(e)
    else:
        caract.append(e)

caract.sort()
nums.sort()
lista= caract+nums
print(lista)
