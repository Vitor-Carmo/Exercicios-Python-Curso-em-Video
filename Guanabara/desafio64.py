numero = soma = 0
while numero!= 999:
    numero = int(input("Digite um número: "))
    if numero != 999:
        soma += numero
print(f"O somatório dos números digitados é {soma}")