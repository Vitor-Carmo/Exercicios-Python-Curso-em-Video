Aluno = dict()
nome = str(input('Nome: '))
Aluno['Nome'] = nome
media = float(input(f'Média do {nome}: '))
Aluno['Média'] = media
for k,v in Aluno.items():
    print(f'{k} é igual a {v}')
print('Situação é igual a ', end='')
if Aluno['Média'] > 7:
    print('Aprovado!')
else:
    print('Reprovado!')
