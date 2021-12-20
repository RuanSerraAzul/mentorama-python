setx = set(["apple","mango"])
sety = set(["mango","orange"])
setz = set(["mango"])

#faça a união dos três conjuntos e imprima o resultado

itens = setx|sety|setz
print (itens)




##Verifique quais elementos comuns do conjunto setx e sety e imprima o resultado
print("O elemento de setx que aparece em sety é",set(setx)&(sety))



###Verifique se o conjunto setx é subconjunto do conjunto sety e setz utilizando issubset()

if setx.issubset(sety) == True:
    print("Setx é subconjunto de sety")
else:
    print("Setx não é subconjunto de sety")


if setx.issubset(setz) == True:
    print("Setx é subconjunto de setz")
else:
    print("Setx não é subconjunto de setz")



####Verifique quais os elementos do conjunto setx não existem em sety
print ("Os elementos que existem em setx e não existem em sety são", setx.difference(sety))

