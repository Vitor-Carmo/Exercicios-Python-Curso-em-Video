from datetime import date
funcionario = {}
ano_atual = date.today().year
funcionario['nome'] = str(input('Nome: '))
funcionario['idade'] = ano_atual - int(input('Ano de nascimento: '))
funcionario['ctps'] = int(input('Cateira de trabalho (0 se não tem): '))

if not funcionario['ctps'] == 0:
    funcionario['contratação'] = int(input('Ano Contratação: '))
    funcionario['Salário'] = float(input('Salário: R$'))
    funcionario['aposentadoria'] = funcionario['idade'] + ((funcionario['contratação'] + 35) - ano_atual)

print('=-'*20)
for k,v in funcionario.items():
    print(f'- {k} tem o valor {v}')
