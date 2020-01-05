numeros = []
par = []
impar = []
while True:
    i = int(input('Digite um número: '))
    numeros.append(i)
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
    usuario = (input('Quer continuar? [S/N] ')).upper().strip()
    if usuario in 'N':
        break
print('=-'*20)
print(f'lista completa {numeros}')
print(f'lista de pares {par}')
print(f'lista completa dos impares {impar}')
