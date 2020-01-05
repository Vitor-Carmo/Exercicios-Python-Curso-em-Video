tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional',
          'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará',
          'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print("=-" * 20)
print(f"lista do dos time do brasileirão 2019 {tabela} ")
print("=-" * 20)
print(f"Os 5 primeiros são {tabela[0:5]}")
print("=-" * 20)
print(f"os quatro últimos são {tabela[-4:]}")
print("=-" * 20)
print(f"Times em ordem alfabética: {sorted(tabela)}")
print("=-" * 20)
print(f"O Chapecoense está na {tabela.index('Chapecoense')+1}º posição")