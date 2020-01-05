from desafio112.utilidadescv import moeda
from desafio112.utilidadescv import dado
preco = dado.leia_dinheiro(input('Digite um preço:'))
moeda.resumo(preco, 100, 100)
