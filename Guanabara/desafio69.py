Maior_dezoito = Homens = Mulheres_vinte = 0
while True:
    idade = int(input("Digite uma idade: "))
    sexo = str(input("Digite um sexo [M/F]: ")).upper().strip()[0]

    while sexo != "M" and sexo != "F":
        sexo = str(input("Digite um sexo [M/F]: ")).upper().strip()[0]

    if idade > 18:
        Maior_dezoito += 1
    if sexo in "M":
        Homens += 1
    if sexo == "F" and idade < 20:
        Mulheres_vinte += 1

    Continuar = str(input("Quer continiuar? [S/N]: ")).upper().strip()[0]
    while Continuar != "S" and Continuar != "N":
        Continuar = str(input("Quer continiuar? [S/N]: ")).upper().strip()[0]

    if Continuar == "N":
        break
print(f"O total de pessoas com Mais de 18 anos é {Maior_dezoito}")
print(f"Ao todo temos {Homens} homens cadastrados")
print(f"E temos {Mulheres_vinte} mulheres com menos de 20 anos")
