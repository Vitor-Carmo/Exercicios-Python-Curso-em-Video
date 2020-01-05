from desafio109 import moeda
preco = float(input('Digite um preço: '))
print(f'A Metade de {moeda.moeda(preco)} é {moeda.metade(preco,True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco,True)} ')
print(f'Aumentando 10% de {moeda.moeda(preco)} temos {moeda.aumentar(preco,10,True)} ')
print(f'Diminuindo 13% de {moeda.moeda(preco)} temos {moeda.diminuir(preco,13,True)} ')
