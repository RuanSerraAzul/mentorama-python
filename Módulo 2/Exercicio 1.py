
conjunto = list()
pessoas = dict()
media = 0
soma = media
while True:
    pessoas.clear()
    # Leitura dos dados de uma pessoa
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO!apenas os caracteres M ou F são aceitos.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    conjunto.append(pessoas.copy())
    # cópiando dicionário pessoas para a lista conjunto
    while True:
        continuar = str(input('Quer continuar: [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! apenas os caracteres S ou N são aceitos.')
    if continuar == 'N':
        break
print("=-=" * 15)
print(f'A) Temos {len(conjunto)} pessoas cadastradas.')
media = soma / len(conjunto)
print(f'B) A média de idade geral é {media:5.2f} anos.')
print('C) Nomes das mulheres cadastradas: ', end='')
for p in conjunto:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in conjunto:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('______---------=========FIM DO PROGRAMA=========---------______')