MaiorPeso = MenorPeso = 0
for i in range(0,5):
    peso = float(input("Digite seu peso: "))
    if i == 1:
        MenorPeso = peso

    if peso > MaiorPeso:
        MaiorPeso = peso

    if MenorPeso > peso:
        MenorPeso = peso


print("o Maior peso foi {}kg.\no Menor peso foi {}kg".format(MaiorPeso,MenorPeso))