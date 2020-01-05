def leia_int(numero):

    while not numero.isnumeric():
        print("\033[0;31mERRO! Digite um número válido: ")
        numero = input('\033[mDigite um número: ')
    else:
        return numero


n = leia_int(input('Digite um número: '))
print(f"Você acabou de digitar o número {n}")

