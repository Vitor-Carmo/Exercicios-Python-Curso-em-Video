from desafio108 import moeda
preco = float(input('Digite um preço: '))
print('A Metade de {} é {}'.format(moeda.moeda(preco), moeda.moeda(moeda.metade(preco))))
print('O dobro de {} é {} '.format(moeda.moeda(preco), moeda.moeda(moeda.dobro(preco))))
print('Aumentando 10% de {}, temos {} '.format(moeda.moeda(preco), moeda.moeda(moeda.aumentar(preco,10))))
print('Diminuindo 13% de {}, temos {} '.format(moeda.moeda(preco), moeda.moeda(moeda.diminuir(preco,13))))
