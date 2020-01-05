from random import randint

Maior_valor = Menor_valor = 0
Valores_sorteados = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f"Os valores sorteados foram: ", end=' ')
for i, sorteados in enumerate(Valores_sorteados):
    print(sorteados, end=" ")

    if i == 0:
        Maior_valor = Menor_valor = sorteados
    else:
        if Maior_valor < sorteados:
            Maior_valor = sorteados

        if Menor_valor > sorteados:
            Menor_valor = sorteados

print(f"\nO Maior Número foi lido {Maior_valor}")
print(f"E o menor valor lido foi {Menor_valor}")
