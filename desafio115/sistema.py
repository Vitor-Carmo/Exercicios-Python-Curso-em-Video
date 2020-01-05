from desafio115.lib.arquivo import *
from time import sleep

arquivo = 'cadastrados.txt'
if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)


while True:
    usuario_resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    if usuario_resposta == 1:
        ler_arquivo(arquivo)

    elif usuario_resposta == 2:
        cabeçalho('\033[32mNOVO CADASTRO\033[m')
        nome = str(input('Nome: '))
        idade = leia_int('idade: ')
        cadastrar(arquivo, nome, idade)

    elif usuario_resposta == 3:
        cabeçalho('\033[36mSaindo do sistema... Até logo!\033[m')
        break

    else:
        print('\033[31mERRO! Digite uma opção valida, por favor.\033[m')
    sleep(1)
