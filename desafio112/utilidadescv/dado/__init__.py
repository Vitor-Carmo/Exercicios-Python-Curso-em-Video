def leia_dinheiro(msg):
    valido = False
    entrada = str(msg).replace(',', '.').strip()
    while not valido:
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! \"{entrada}\" não é um valor valido!\033[m')
            entrada = str(input('Digite um preço: ')).replace(',','.')
        else:
            valido = True
            return float(entrada)
