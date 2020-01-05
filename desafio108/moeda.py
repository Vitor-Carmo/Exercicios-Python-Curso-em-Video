def metade(d):
    d = d / 2
    return d


def dobro(d):
    d = d * 2
    return d


def aumentar(d, porcent):
    porcentagem = d + (d * porcent/100)
    return porcentagem


def diminuir(d, porcent):
    porcentagem = d - (d * porcent/100)
    return porcentagem


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

