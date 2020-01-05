jogador = {}
goals = []
total_goals = 0

jogador['nome'] = str(input('Nome do jogador: '))

total_partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

for i in range(total_partidas):
    goals.append(int(input(f'   Quantas gols na partida {i}? ')))
    total_goals += goals[i]

jogador['goals'] = goals[:]

jogador['total'] = total_goals  # sum(goals)

print('-=' * 20)
print(jogador)
print('-=' * 20)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v} ')

print('-=' * 20)

print(f'O jogador {jogador["nome"]} jogor {len(jogador["goals"])} partidas.')
for i in range(total_partidas):
    print(f'    => Na partida {i} fez {jogador["goals"][i]} goals')

print(f'foi no total {total_goals} goals')
