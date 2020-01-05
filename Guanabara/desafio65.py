numero = soma = i = Maior_numero = 0
continuar = "S"
x = True
while continuar == "S":
    numero = int(input("Digite um número: "))
    if x:
        Menor_numero = numero
        x = False

    if numero > Maior_numero:
        Maior_numero = numero

    if numero < Menor_numero:
        Menor_numero = numero

    soma += numero
    i+=1
    continuar = str(input("Quer Continuar? [S/N]")).upper().strip()[0]


Media = soma/i
print("A média dos números digitados é {}"
      "\nO MAIOR número foi {} e o MENOR número foi {}".format(Media,Maior_numero,Menor_numero))