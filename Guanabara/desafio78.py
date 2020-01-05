Maior_valor = Menor_valor = 0

valores = []
for i in range(5):
    valores.append(int(input(f"Digite um valor na posição {i}: ")))
    if i == 0:
        Menor_valor = Menor_valor = valores[i]
    else:
        if Maior_valor< valores[i]:
            Maior_valor = valores[i]
        if Menor_valor > valores[i]:
            Menor_valor = valores[i]
print("=-"*20)
print("Você digitou {}".format(valores))
print("O maior valor Digitado foi {} nas posições ".format(Maior_valor),end='')
for i in range(len(valores)):
    if valores[i] == Maior_valor:
        print(i,end='.. ')
print("\nO menor valor Digitado foi {} nas posições ".format(Maior_valor),end='')
for i in range(len(valores)):
    if valores[i] == Menor_valor:
        print(i,end='.. ')