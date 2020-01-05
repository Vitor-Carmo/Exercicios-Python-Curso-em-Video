from desafio115.lib.interface import *


def arquivo_existe(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        arq = open(nome,'wt+')
        arq.close()
    except:
        print('\033[31mErro na criação do arquivo!\033[m')
    else:
        print(f'Arquivo {nome} foi criado com sucesso')


def ler_arquivo(nome):
    try:
        arq = open(nome,'rt')
    except:
        print('\033[31mErro na leitura do arquivo.\033[m')
    else:
        cabeçalho('\033[36mPESSOAS CADASTRADAS\033[m')
        for linha in arq:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:3>} anos')
    finally:
        arq.close()


def cadastrar(nome_arq, name="DescONHECIDO ", age=0):
    try:
        arq = open(nome_arq,'at')
    except:
        print('Houve algum na abertura do arquivo.')
    else:
        try:
            arq.write(f'{name};{age}\n')
        except:
            print('Houve algum erro na hora de escrever os arquivos.')
        else:
            print(f'\033[32mNovo registro de {name} adicionado\033[m')
            arq.close()