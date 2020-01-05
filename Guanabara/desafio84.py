pessoas = []
individuo = []
Maior_peso = Menor_peso = 0
while True:
    individuo.append(str(input('Nome: ')))
    individuo.append(float(input('Peso: ')))
    pessoas.append(individuo[:])

    if len(pessoas) == 1:
        Maior_peso = Menor_peso = individuo[1]
    else:
        if Maior_peso < individuo[len(individuo)-1]:
            Maior_peso = individuo[len(individuo)-1]

        if Menor_peso > individuo[len(individuo)-1]:
            Menor_peso = individuo[len(individuo)-1]

    individuo.clear()

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar in 'N':
        break

print('=='*20)

print(f'No total teve {len(pessoas)} pessoas cadastradas.')

print(f'O maior peso foi de {Maior_peso}kg. ',end='')
for p in pessoas:
    if Maior_peso in p:
        print(f'[{p[0]}]', end=' ')

print(f'\nO menor peso foi de {Menor_peso}kg. ',end='')
for p in pessoas:
    if Menor_peso in p:
        print(f'[{p[0]}]',end=' ')