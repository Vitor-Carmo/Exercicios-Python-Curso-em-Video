lista = []
while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('O valor digitado já existe na lista. Tente outro.')

    continuar = str(input("Quer Continuar? [S/N] ")).strip().upper()[0]
    if continuar in 'N':
        break
print('-'*20)
lista.sort()
print(lista)
print('-'*20)