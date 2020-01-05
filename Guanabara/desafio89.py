ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])

    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar in 'N':
        break

print('=-' * 20)
for i, aluno in enumerate(ficha):
    print(f'{i:<4} {aluno[0]:<10} {aluno[2]:>8.1f}')
print('=-' * 20)

while True:
    Escolha_usuario = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if Escolha_usuario == 999:
        break
    print('--'*20)
    print(f'Notas de {ficha[Escolha_usuario][0]} são {ficha[Escolha_usuario][1]}')
    print('--' * 20)
