from datetime import date
year = date.today().year

MaiorDeIdade = 0
MenorDeIdade = 0

for i in range(0,7):
    ano = int(input("Digite seu ano de nascimento: "))
    idade =  year - ano
    if idade >= 18:
        MaiorDeIdade += 1
    else:
        MenorDeIdade += 1

print('''{} são MAIORES de idade. 
{} são MENORES de idade.'''.format(MaiorDeIdade,MenorDeIdade))