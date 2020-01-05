from random import randint
from time import sleep

jogos = []
jogo = []
Quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie: '))
for i in range(Quantidade_jogos):
    while not len(jogo) == 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()

print('=-' * 20)
for i, j in enumerate(jogos):
    print(f'Jogo {i + 1}: {j}')
    sleep(0.5)
print('=-' * 20)
