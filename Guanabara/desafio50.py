soma = 0
for i in range(0,6):
    n = int(input("Digite o {}° numero: ".format(i+1)))
    if n%2 == 0:
        soma += n
print(soma)
