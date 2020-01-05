def voto(nasc):
    """
    :param nasc: it's someone's birth year
    :return: if this person can vote or not
    """

    age = idade(nasc)

    if age < 16:
        return 'NEGADO'
    elif 16 <= age < 18 or age > 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


def idade(age):
    from datetime import date
    birth = age
    year = date.today().year
    return year - birth


print('=-'*20)
ano_nasc = int(input('Em que ano você nasceu?: '))
print(f'Com {idade(ano_nasc)} anos o voto é: {voto(ano_nasc)}')
