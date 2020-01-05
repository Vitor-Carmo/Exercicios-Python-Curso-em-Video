numeros = [[], []]
for i in range(7):
    n = int(input('Digigite o {}° número: ').format(i + 1))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('=='*20)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores Pares digitados foram:  {numeros[0]}')
print(f'Os valores Ímpares digitados foram: {numeros[1]}')
