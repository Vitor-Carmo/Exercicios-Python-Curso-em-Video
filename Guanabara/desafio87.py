matriz = [[0]*3, [0]*3, [0]*3]
Soma_pares = Soma_3_coluna= Maior_linha =0
for i in range(3):
    for j in range(3):
        matriz[i][j]=(int(input(f'Digite um valor para [{i}, {j}]: ')))
        if matriz[i][j] % 2 == 0:
            Soma_pares += matriz[i][j]

        if j == 2:
            Soma_3_coluna += matriz[i][j]

        if Maior_linha < matriz[1][j] and i == 1 or j == 0:
            Maior_linha = matriz[1][j]

print('=-'*20)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]}]', end=' ')
    print()
print('=-'*20)

print(f'A soma dos valores pares é {Soma_pares}.')
print(f'A soma dos valores da terceira coluna é {Soma_3_coluna}.')
print(f'O Maior Valor da segundo linha é {Maior_linha}.')