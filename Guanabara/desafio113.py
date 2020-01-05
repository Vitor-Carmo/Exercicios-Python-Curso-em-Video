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


def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: digite um valor válido: \033[m')
            continue
        except KeyboardInterrupt:
            print("\033[31mUsuário preferiu não digitar os dados\033[m")
            return 0
        else:
            return n


inteiro = leia_int('Digite um número inteiro:')
real = leia_float('Digite um número real')
print(f'O número inteiro é {inteiro}')
print(f'O número real é {real}')
