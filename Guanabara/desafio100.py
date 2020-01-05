from random import randint


def sorteio(lst):
    for i in range(5):
        lst.append(randint(a=1, b=10))
    print(f"os números sorteados são {lst}")


def soma_maior(lst):
    soma_par = 0
    for n in lst:
        if n % 2 == 0:
            soma_par += n
    print(f"A soma dos números pares é: {soma_par}")


lista = []
sorteio(lista)
soma_maior(lista)
