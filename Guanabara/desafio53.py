frase = str(input("Digite uma frase: ")).split()
frase = ''.join(frase).upper()

menos = len(frase) - 1

for i in range(0, len(frase)):
    if frase[i] == frase[menos]:
        polindromo = True
    else:
        polindromo = False
        break
    menos -= 1

if polindromo == True:
    print('A frase é um polindromo!')
else:
    print('A frase não é um polindromo!')