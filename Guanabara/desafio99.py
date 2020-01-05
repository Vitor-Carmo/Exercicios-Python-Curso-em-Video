def maior(*n):
    maior_valor = 0
    print('=-'*20)
    print('Analisando os valores: ')
    for v in n:
        print(f'{v}', end=' ')
        if n.index(v) == 0:
            maior_valor = v
        else:
            if v > maior_valor:
                maior_valor = v
    print(f"\nde {len(n)}  valores inseridos o maior valor é {maior_valor}.")


maior(1, 2, 3, 4, 5)
maior(15, 531, 521, 5536, 1000)
maior(1351, 564156, 1311161, 2253, 15615)
maior(1, 2)
