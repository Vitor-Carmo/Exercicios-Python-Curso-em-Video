Total_gasto = Produto_mil = Mais_barato = 0
Nome_produto_mais_barato = str
Variavel_pra_dar_certo = True
while True:
    Nome_produto = str(input("Nome do Produto: "))
    Preco = float(input("Digite o preço do produto: R$"))
    if Variavel_pra_dar_certo:
        Mais_barato = Preco
        Nome_produto_mais_barato = Nome_produto

    Total_gasto += Preco

    if Preco > 1000:
        Produto_mil += 1

    if Preco < Mais_barato:
        Mais_barato = Preco
        Nome_produto_mais_barato = Nome_produto
        Variavel_pra_dar_certo = False
    Continuar = str(input("Quer continiuar? [S/N]: ")).upper().strip()[0]
    while Continuar != "S" and Continuar != "N":
        Continuar = str(input("Quer continiuar? [S/N]: ")).upper().strip()[0]

    if Continuar == "N":
        break

print(f"O total da compra foi R${Total_gasto}")
print(f"Temos {Produto_mil} produtos custando mais de R$1000")
print(f"O produto mais barato foi {Nome_produto_mais_barato} que custa {Mais_barato}")
