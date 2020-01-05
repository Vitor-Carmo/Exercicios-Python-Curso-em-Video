numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezeseis', 'dezessete',
           'dezoito',
           'dezenove', 'vinte')
while True:
    numero = int(input("Digite um número entre 0 e 20: "))
    while not 0 <= numero <= 20:
        print("Tente novamente.", end=" ")
        numero = int(input("Digite um número entre 0 e 20: "))
    else:
        print("Você digitou o número {} ".format(numeros[numero]))
        break

