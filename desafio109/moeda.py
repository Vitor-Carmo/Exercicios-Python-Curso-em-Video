def metade(d=0, m=False):
    d = d / 2
    if m is False:
        return d
    else:
        return moeda(d)


def dobro(d=0, m=False):
    d = d * 2
    if m is False:
        return d
    else:
        return moeda(d)


def aumentar(d=0, porcent=0, m=False):
    porcentagem = d + (d * porcent/100)
    if m is False:
        return porcentagem
    else:
        return moeda(porcentagem)


def diminuir(d=0, porcent=0, m=False):
    porcentagem = d - (d * porcent/100)
    if m is False:
        return porcentagem
    else:
        return moeda(porcentagem)


def moeda(preco=0.00, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

