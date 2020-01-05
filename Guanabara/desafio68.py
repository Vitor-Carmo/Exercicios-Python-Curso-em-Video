from random import randint

print("=-" * 20, "\nVAMOS JOGAR PAR OU IMPAR\n" + "=-" * 20)
quantidade_Venceu = 0

while True:
    Computador = randint(0, 10)
    Jogador_numero = int(input("Digite um valor: "))
    Par_ou_impar = str(input("Par ou Impar? [P/I]: ")).strip().upper()[0]

    while Par_ou_impar != "P" and Par_ou_impar != "I":
        print("=-" * 20)
        print("JOGADA INVALIDA!!! \ntente novamente")
        print("=-" * 20)
        Par_ou_impar = str(input("Par ou Impar? [P/I]: ")).strip().upper()[0]

    Jogada = Jogador_numero + Computador

    if Jogada % 2 == 0:
        resultado = "PAR"
        if Par_ou_impar in "P":
            acertou = True
            quantidade_Venceu += 1
        else:
            acertou = False
    else:
        resultado = "IMPAR"
        if Par_ou_impar in "I":
            acertou = True
            quantidade_Venceu += 1
        else:
            acertou = False

    print("-" * 40)
    print("Você jogou {} e o computador {}. Total de {} deu {}".format(Jogador_numero, Computador, Jogada, resultado))
    print("-" * 40)
    if acertou:
        print("VOCÊ VENCEU!!!\n")
        print("Vamos Jogar novamente.\n")
    else:
        print("VOCÊ PERDEU!!!\n")
        print("GAME OVER! Você venceu {} vezes!".format(quantidade_Venceu))
    print("=-" * 20)

    if acertou is False:
        break
