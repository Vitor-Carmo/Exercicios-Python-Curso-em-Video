from random import randint

palpites = 0

computador = randint(0,10)
print("-=-"*20)
print("Pensei em um número de 0 até 10, tente adivinhar qual é:")
print("-=-"*20)

n =int(input())

while n != computador:

    n = int(input("Tente Novamente!\n"))
    palpites +=1
else:
    print("Parabéns, você venceu! o número era {} e você deu {} palpites.".format(computador,palpites))