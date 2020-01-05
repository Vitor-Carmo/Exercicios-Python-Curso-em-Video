'''def par(x):
    if x % 2 == 0:
        return 'Par'


tupla = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')), int(input('Digite o ultimo número: ')))

print("Você digitou os valores {} ".format(tupla))
print("O 9 aparaceu {} vezes".format(tupla.count(9)))
if 3 in tupla:
    print("O primeiro valor três foi digitado na {}º posição ".format(tupla.index(3) + 1))
else:
    print("O valor 3 não foi digitado em nenhuma posição")
print("Os números pares são: ", end='')
for i in tupla:
    if par(i) == "Par":
        print(i, end=" ")
'''
import math
num = (int(input('Digite um número')),
           int(input('Digite um número')),
               int(input('Digite um número')),
                   int(input('Digite um número')))

print(f'O número 9 apareceu {num.count(9)} vezes\n')
print(f'O número 3 apareceu pela primeira vez na posição {num.index(3)}\n')

for i in range(0,4):
    if num[i] % 2 == 0:
        print(f'Os números pares da tupla foram: {num[i]}',end = ' ')

print('')