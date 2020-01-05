from time import sleep

def contagem(inicio, fim, passo):
    print('=-' * 20)
    if passo == 0:  # se o passo for 0 será considerado 1
        passo = 1
    passo = abs(passo)  # pegando o valor absoluto do passo, ou seja, o possitivo dele.
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        passo = -passo
        fim -= 1
    else:
        fim += 1
    for i in range(inicio, fim, passo):
        sleep(0.4)
        print(i, end=' ')
    print("Fim!")


contagem(1, 10, 1)
contagem(10, 1, 1)
print('=-' * 20)
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contagem(inicio, fim, passo)
