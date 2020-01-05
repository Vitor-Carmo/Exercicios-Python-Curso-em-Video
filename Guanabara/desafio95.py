jogadores = []
jogador = {}
goals = []

while True:
    jogador['nome'] = str(input('Nome do jogador: '))

    total_partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    goals.clear()
    for i in range(total_partidas):
        goals.append(int(input(f'   Quantas gols na partida {i+1}? ')))

    jogador['goals'] = goals[:]
    jogador['total'] = sum(goals)

    jogadores.append(jogador.copy())
    jogador.clear()

    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        print('ERRO! responda apenas S ou N.')
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break

print('=-' * 20)
for i, j in enumerate(jogadores):
    print(f'{i:<4} {j["nome"]:<} {j["goals"]:} {j["total"]:>6}')
print('=-' * 20)

while True:
    resp = int(input('Mostra o dado de qual jogador: (999 para para): '))
    if resp == 999:
        break
    if resp >len(jogadores)-1:
        print('Jogador não existe')
    else:
        print(f'--LEVATAMENTO DO JOGADOR {jogadores[resp]["nome"]}: ')
        for i, j in enumerate(jogadores[resp]['goals']):
            print(f'Na Partida {i+1} fez {j} gols')
    print("-"*40)
