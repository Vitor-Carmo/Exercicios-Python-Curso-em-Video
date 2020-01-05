n1 = int(input("Digite um número:"))
n2 = int(input("Digite um segundo número:"))


Desição = 0

while Desição != 5:
    Desição=int(input('''
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA \n'''))

    if Desição == 1:
        print("{} + {} = {}".format(n1,n2,n1+n2))
    if Desição == 2:
       print("{} X {} = {} ".format(n1,n2, n1*n2))
    if Desição == 3:
        if n1>n2:
            print("Entre {} e {}, {} é Maior".format(n1,n2,n1))
        elif n2>n1:
            print("Entre {} e {}, {} é Maior".format(n1,n2,n2))
        else:
            print("Ambos possui o mesmo valor.")

    if Desição == 4:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite um segundo número: "))
    else:
        print("Número invalido.")
print("Saindo...")
