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


def resumo(preco=0,aumen=0, dimi=0):
    print('-'*30)
    print(f'{"RESUMO VALOR":^30}')
    print('-'*30)
    print(f'{"Preso analizado:":<20}{moeda(preco):<20}')
    print(f'{"Dobro do preço:":<20}{dobro(preco, True):<20}')
    print(f'{"Metade do preço:":<20}{metade(preco, True):<20}')
    print(f'{f"{aumen}% de aumento:":<20}{aumentar(preco, aumen, True):<20}')
    print(f'{f"{dimi}% de aumento:":<20}{diminuir(preco,dimi ,True):<20}')
    print('-'*30)
    #\t -> tabulação
