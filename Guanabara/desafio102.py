def fatorial(n, show=False):
    """
        => Calcula o número de um fatorial

    :param n: O número do fatorial
    :param show: mostrar conta do fatorial. defaut = False
    :return: o fatorial do numero digitado
    """

    f = 1
    if show is False:
        for i in range(n, 0, -1):
            f *= i
        return f
    else:
        for i in range(n, 0, -1):
            f *= i
            if i == 1:
                print(f"{i} = ", end='')
            else:
                print(f"{i} X ", end='')
        return f
    # Eu posso simplificar bastante até


print('=-'*20)
print(fatorial(5, show=True))
print(fatorial(5))
