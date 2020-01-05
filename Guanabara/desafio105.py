def notas(*nota, sit=False):
    """
    => Avaliar a situação nota e situação de vários alunos

    :param nota: as nostas do alunos para serem avaliadas
    :param sit: um parâmetro opcional, verifica se a situação do aluno é BOA, RAZOAVEL ou RUIM
    :return: um dicionário contendo a situação do aluno

    """

    ficha = {}
    maior = menor = 0
    for i, n in enumerate(nota):
        if i == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n

    media = sum(nota)/len(nota)

    ficha['total'] = len(nota)
    ficha['maior'] = maior
    ficha['menor'] = menor
    ficha['média'] = media
    if sit is True:
        if media >= 7:
            ficha['situação'] = 'BOA'
        elif media >= 5:
            ficha['situação'] = 'RAZOAVEL'
        else:
            ficha['situação'] = 'RUIM'

    return ficha


resp = notas(6, 7, 9, 9, 9, 0, 0, 0)
print(resp)

