numeros = list()
while True:
    numeros.append(int(input("Digite um número: ")))
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()
    if continuar in 'N':
        break
print('=-'*20)
print('Você digitou {} elementos'.format(len(numeros)))
numeros.sort(reverse=True)
print('Os valores em ordem decrescente são {}'.format(numeros))
if 5 in numeros:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 não foi encontrado em nenhuma pisição.")