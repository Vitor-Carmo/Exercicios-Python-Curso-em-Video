palavras = ('Programar', 'Jogar', 'Codificar', 'Imaginar', 'Louvar', 'Adorar')
for palavra in palavras:
    print(f"\nA palavra {palavra.upper()} Tem as vogais: ", end=' ')
    for i in range(0, len(palavra)):
        if palavra[i].upper() in "AEIOU":
            print(palavra[i].lower(), end=" ")
