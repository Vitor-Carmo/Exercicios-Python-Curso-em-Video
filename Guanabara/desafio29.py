km = float(input("Digite a velocidade do carro: "))
if km > 80.00:
    km = (km-80)*7.00
    print("VOCÊ UTRAPASSOU O LIMITE DE VELOCIDADE! \nvocê deve pagar uma multa de R${}.".format(km))
else:
    print("Tenha um bom dia! Dirije com segurança!")
