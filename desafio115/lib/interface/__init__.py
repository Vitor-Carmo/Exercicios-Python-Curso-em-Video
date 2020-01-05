def line(lenn = 42):
    return '\33[33m-\33[m'*lenn


def cabeçalho(msg):
    print(line())
    print(msg.center(42))
    print(line())


def menu(lista):
    cabeçalho('\033[36mMENU PRINCIPAL\033[m')
    for i, item in enumerate(lista):
        print(f'\033[32m{i+1} - \033[35m{item}\033[m')
    print(line())
    resposta = leia_int('\033[32mSua Opção:\033[m ')
    return resposta


def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: digite um valor válido:\033[m ')
            continue
        except KeyboardInterrupt:
            print("\033[31mUsuário preferiu não digitar os dados\033[m")
            return 0
        else:
            return n