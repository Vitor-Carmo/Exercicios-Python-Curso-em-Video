def pyhelp():
    while True:
        from time import sleep
        linhas("SYSTEMA DE AJUDA PyHELP")
        sleep(0.1)
        comando = str(input('Função po biblioteca >>> ')).lower().strip()
        if comando == 'fim':
            break
        linhas(f"Acesando o Comando {comando}")
        sleep(0.3)
        print('\033[0;30;45m')
        help(comando)
        sleep(0.3)


def linhas(msg):
    tam = len(msg) + 4
    print("\033[0;30;43m~" * tam)
    print(f'  {msg}')
    print("~" * tam)
    print('\033[m', end='')


pyhelp()
