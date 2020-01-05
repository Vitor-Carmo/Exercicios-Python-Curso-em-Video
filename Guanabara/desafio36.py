casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário do comprador:"))
ano = int(input("Quantos anos ele vai pagar? "))


mes = ano*12
prestacao =  casa/mes
minimo =salario*30/100 

print("Você ganha {:.2f} e deve pagar {:.2f} por mês até completar o valor da casa em {} anos".format(salario,prestacao,ano))

if(prestacao<=minimo):
    print("Emprestimo aceito")
else:
    print("Emprestimo Negado")


