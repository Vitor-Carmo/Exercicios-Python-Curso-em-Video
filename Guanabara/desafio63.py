b = i = 1
a = 0
termos  = int(input("Digite a quantidade de termos: "))
print(a,b, end=' ')
while i <= termos-2:
    c = a + b
    print(c, end=' ')
    a = b
    b = c
    i += 1