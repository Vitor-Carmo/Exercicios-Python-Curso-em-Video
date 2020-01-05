n = int(input("Digite um número: "))
fatorial = 1
i = n
while i > 1:
    fatorial *= i
    i -= 1
print("{}! = {}".format(n, fatorial))
