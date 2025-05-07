palavra = ""     # -> você colocar aqui a palavra que você quer que apareça pra acerta
tentativas = 6   # OBS: coloque só em letra maiúscula!
letras_adivinhadas = []

while tentativas > 0:
    palavra_oculta = ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra])
    print(palavra_oculta)

    if palavra_oculta == palavra:
        print("você venceu!")
        break

    chute = input("Letra: ").lower()
    if chute in palavra:
        letras_adivinhadas.append(chute)
    else:
        tentativas -= 1
        print(f"Errou! tentativas restantes: {tentativas}")