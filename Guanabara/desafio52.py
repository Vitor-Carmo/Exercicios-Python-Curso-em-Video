n = int(input('Digite um número: '))
TotalPrimos  = 0
for i in range(1,n+1):
    if n%i ==0:
        TotalPrimos+=1
if TotalPrimos == 2:
    print("{} é um número primo. ".format(n))
else:
    print("{} não é um número primo. ".format(n))