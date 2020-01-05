a1 = int(input('Digite o primeiro termo da PA:'))
razão = int(input('Digite a razão da PA: '))
Quantidade_termos = 10
while Quantidade_termos!=0:
    i = 1
    while i <= Quantidade_termos:
        print(a1)
        a1 += razão
        i += 1
    Quantidade_termos = int(input("Quantos termo a mais você quer ver? "))