numero = soma = quantidade_numero = 0
while True:
    numero = int(input("Digite um valor (999 para parar): "))
    if numero == 999:
        break
    soma += numero
    quantidade_numero += 1
print(f"A soma dos {quantidade_numero} valores foi {soma}!")