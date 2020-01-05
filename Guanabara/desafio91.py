from random import randint
from time import sleep
from operator import itemgetter

raking = []
jogadores = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
aux = int
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)

print('=-' * 20)

print(f'{"<<RANKING JOGADOR>>":^30}')
raking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(raking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}')
    sleep(0.5)
