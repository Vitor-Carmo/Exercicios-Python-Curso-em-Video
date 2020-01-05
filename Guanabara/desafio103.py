def ficha(j='', gols=0):

    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f"O jogador {'<desconhecido>' if j.strip() == '' else j} fez {gols} gol(s) no Campeonato")


nome = str(input('Nome do jogador: '))
num_goals = input('Número de goals: ')


ficha(nome, num_goals)
