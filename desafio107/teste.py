from desafio107 import moeda
preco = float(input('Digite um preço: '))
print('A Metade de {} é {}'.format(preco, moeda.metade(preco)))
print('O dobro de {} é {} '.format(preco,moeda.dobro(preco)))
print('Aumentando 10% de {}, temos {} '.format(preco,moeda.aumentar(preco,10)))
print('Diminuindo 13% de {}, temos {} '.format(preco,moeda.diminuir(preco,13)))
