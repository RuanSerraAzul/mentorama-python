##Considere a string s=Mentorama, escreva um programa que:
## Converta a string para maiusculo, em seguida
## imprima a de trás pra frente
## imprima somente as vogais

def ChecarVogais(string, vogais): 
    result = [each for each in string if each in vogais]  
    print(result)  
s = "Mentorama"
print(s.upper())
print(s[::-1])
vogais = "aeiou"
ChecarVogais(s, vogais); 