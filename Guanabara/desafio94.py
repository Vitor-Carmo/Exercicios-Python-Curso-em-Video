pessoas = []
individuo = {}
mulheres = []
soma = 0

while True:
    individuo['nome'] = str(input('Nome: '))

    individuo['sexo'] = str(input('Sexo: [M/F] ').upper().strip())[0]
    while individuo['sexo'] not in 'MF':
        print('ERRO! por favor digite apenas M ou F')
        individuo['sexo'] = str(input('Sexo: [M/F] ').upper().strip())[0]
    if individuo['sexo'] in 'F':
        mulheres.append(individuo['nome'])

    individuo['idade'] = int(input('Idade: '))
    soma += individuo['idade']
    pessoas.append(individuo.copy())
    individuo.clear()

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('ERRO! responda apenas S ou N.')
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break

print('-=' * 20)

media = soma / len(pessoas)

print(f'A)  Ao todo temos {len(pessoas)} pesoas cadastradas')

print(f'B)  A média de idade é {media:5.2f} anos')

print(f'C)  As mulheres cadastradas foram: ', end='')
for mulher in mulheres:
    print(f'{mulher}', end=' ')
print()

print(f'D)  Lista de pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] > media:
        print('   ',end='')
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')
    print()
print('ENCERRANDO O PROGRAMA...')
