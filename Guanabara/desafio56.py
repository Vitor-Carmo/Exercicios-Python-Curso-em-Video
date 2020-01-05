SomaIdade = 0
MaisVelho = 0
Quantidade_mulher = 0
for i in range(0,4):
    nome = str(input("Digite o seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo M/F: ")).upper()

    SomaIdade += idade

    if sexo == "M" and idade > MaisVelho:
        MaisVelho = idade
        NomeVelho = nome


    if sexo == "F" and idade < 20:
        Quantidade_mulher += 1

Media = SomaIdade/4


print('''A média da idade do grupo é {}
O Homem mais velho é {}
E a quantidade de mulheres com menos de 20 anos é {}'''.format(Media,NomeVelho,Quantidade_mulher))