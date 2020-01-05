#DESAFIO 28
from random import randint
from time import sleep
computador = randint(0,5)
print("-=-"*20)
print("Pensei em um número de 0 até 5, tente adivinhar qual é:")
print("-=-"*20)
n =int(input())
print("PROCESSANDO")
sleep(1)
if n == computador:
    print("Parabéns, você venceu!")
else:
    print("Você Perdeu! \no número era {}".format(computador))